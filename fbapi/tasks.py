from .apicalls import *
from .models import *

def pageData():
    data = FbProfile.objects.all()
    for i in data:
        print(i.FbuserId)
        page_info(str(i.FbuserId), str(i.Fbusertoken))


def postData():
    data = FbProfile.objects.all()
    for i in data:
        post_info(str(i.Fbusertoken))

def CommData():
    data = FbProfile.objects.all()
    for i in data:
        comment_info(str(i.Fbusertoken), str(i.id))
