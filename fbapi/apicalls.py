import requests
import json
from .models import *



def PageLink(uid, atoken):
    utoken = requests.get("https://graph.facebook.com/v9.0/oauth/access_token?grant_type=fb_exchange_token&client_id=140906937800965&client_secret=46d38cdb89cb0c671eb836d59a2b3aa6&fb_exchange_token="+str(atoken)).json()
    lutoken = utoken['access_token']
    data= requests.get("https://graph.facebook.com/v9.0/"+str(uid)+"/accounts?fields=access_token%2Cid%2Cname&access_token="+str(lutoken)).json()
    return data

def page_info(uid, AToken):
    print('Page Functions')
    info = requests.get("https://graph.facebook.com/v9.0/me?fields=username%2Cname%2Cfan_count%2Cabout&access_token="+AToken)
    dataa = info.json()
    print(dataa)
    pname = dataa['name']
    fcount = dataa['fan_count']
    about = dataa['about']
    if 'username' in dataa:
        purl = "https://www.facebook.com/"+dataa['username']
    else:
        purl = "https://www.facebook.com/"+dataa['name']
    obj = Page.objects.filter(page_id=dataa['id'])
    if obj:
        obj.update(page_name=str(pname),page_fans=str(fcount),page_about=str(about),page_url=str(purl))
    else:
        Page.objects.create(fbU_fid=uid ,page_id=dataa['id'],page_name=str(pname),page_fans=str(fcount),page_about=str(about),page_url=str(purl))


def post_info(AToken):
    post_info = requests.get("https://graph.facebook.com/v9.0/me/posts?limit=70&access_token="+AToken)
    post_data = post_info.json()
    for i in post_data['data']:
        post_id= i['id']
        posts_info = requests.get("https://graph.facebook.com/v9.0/"+post_id+"?fields=message%2Cshares%2Cfull_picture%2Cpermalink_url%2Creactions.summary(total_count)%2Clikes.summary(total_count)%2Ccreated_time&access_token="+AToken)
        posts_data = posts_info.json()
        pageid = Page.objects.get(page_id=posts_data['id'].split('_')[0])
        po_id = str(posts_data['id'].split('_')[1])
        if 'full_picture' in posts_data:
            po_photo = str(posts_data['full_picture'])
        else:
            po_photo = "No Photo in Post"
        if 'message' in posts_data:
            po_message = str(posts_data['message'])
        else:
            po_message = "No Message On Post"
        po_permalink = str(posts_data['permalink_url'])
        po_likes_count = posts_data['likes']['summary']['total_count']
        if 'shares' in posts_data:
            po_shares_count = posts_data['shares']['count']
        else:
            po_shares_count = 0
        po_reaction = posts_data['reactions']['summary']['total_count']
        po_time = str(posts_data['created_time'])
        obj = Posts.objects.filter(post_id=po_id)
        if obj:
            obj.update(page_fid=pageid,post_photo=po_photo,post_message=po_message,post_permalink=po_permalink,post_likes_count=po_likes_count,post_shares_count=po_shares_count,post_reaction=po_reaction,post_time=po_time)
        else:
            Posts.objects.create(page_fid=pageid,post_id=po_id,post_photo=po_photo,post_message=po_message,post_permalink=po_permalink,post_likes_count=po_likes_count,post_shares_count=po_shares_count,post_reaction=po_reaction,post_time=po_time)

def comment_info(AToken,pageId):
    page = Page.objects.filter(fbU_fid=pageId)
    for i in range(len(page)):
        print(page[i].id ,page[i].page_name , page[i].page_id)
        page_id = page[i].page_id
        post = Posts.objects.filter(page_fid=page[i].id)
        for i in range(len(post)):
            poid= str(page_id)+"_"+str(post[i].post_id)
            print(poid)
            com_inf = requests.get("https://graph.facebook.com/v9.0/"+poid+"?fields=comments%7Bcreated_time%2Ccan_like%2Cfrom%2Cmessage%2Ccan_remove%2Ccomment_count%2Ccan_comment%2Cis_private%2Cid%2Clike_count%2Cis_hidden%2Ccan_hide%2Creactions%7Bname%2Cusername%2Ctype%7D%2Ccomments%7Bcan_like%2Cfrom%2Cmessage%2Ccan_remove%2Ccomment_count%2Ccan_comment%2Cis_private%2Cid%2Clike_count%2Cis_hidden%2Ccan_hide%2Creactions%7Bname%2Cusername%2Ctype%7D%7D%7D&access_token="+AToken)
            com_dat = com_inf.json()
            print(com_dat.keys())
            if 'comments' in com_dat.keys():
                for item in com_dat['comments']['data']:
                    ctime = item['created_time']
                    calike = item['can_like']
                    cmessage = item['message']
                    caremove= item['can_remove']
                    cacount = item['comment_count']
                    cacomment = item['can_comment']
                    ciprivate = item['is_private']
                    cid = item['id'].split('_')[1]
                    clikecount = item['like_count']
                    cihidden = item['is_hidden']
                    cahide = item['can_hide']
                    ppfid = Posts.objects.get(post_id=item['id'].split('_')[0])
                    pagefid = Page.objects.get(page_id=page_id)
                    if 'from' in item.keys():
                        cfrom= item['from']['name']
                    else:
                        cfrom = 'No User'

                    obj = Comments.objects.filter(comment_id=cid)
                    if obj:
                        obj.update(comment_from=str(cfrom),posts_fid= ppfid, comment_message= str(cmessage), comment_likes_count= clikecount, comment_time= str(ctime), can_like=calike, can_remove=caremove,comment_count=cacount, can_comment=cacomment, is_private=ciprivate, is_hidden=cihidden,can_hide=cahide)
                    else:
                        Comments.objects.create(page_fid=pagefid,comment_id= cid ,comment_from=str(cfrom),posts_fid=ppfid, comment_message= str(cmessage), comment_likes_count= clikecount, comment_time= str(ctime), can_like=calike, can_remove=caremove,comment_count=cacount, can_comment=cacomment, is_private=ciprivate, is_hidden=cihidden,can_hide=cahide)
            else:
                pass