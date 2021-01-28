from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserregisterForm, UserUpdateForm, ProfileUpdateForm
from tweetapi.models import Tweets
from django.contrib.auth.models import Group
from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from users.tokens import account_activation_token
from django.urls import reverse
from django.contrib.auth import login



# def home(request):
#     context = {
#         'tweets': Tweets.objects.all()
#     }
#     return render(request, 'users/home.html',context)


def register(request):
    if request.method == 'POST':
        form = UserregisterForm(request.POST)
        email = request.POST['email']
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }

            link = reverse('activate', kwargs={
                            'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://'+current_site.domain+link

            email = EmailMessage(
                email_subject,
                'Hi '+user.first_name + ', Please the link below to activate your account \n'+activate_url,
                'noreply@semycolon.com',
                [email],
            )
            email.send(fail_silently=False)
            firstname = form.cleaned_data.get('first_name')
            messages.success(request,f'Your Account has been created! Please Confirm your email to complete registration.'+" " + firstname)
            return redirect('login')
    else:
        form = UserregisterForm()
    return render(request, 'users/register.html', {'form':form})


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None


        if user is not None and  account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            email=user.email
            print(email)
            email_subject = 'Welcome To HODOS'

            email = EmailMessage(
                email_subject,
                'Hi '+user.first_name + ', Welcome to HODOS Here You Can Enjoy Your Work \n',
                'noreply@semycolon.com',
                [email],
            )
            email.send(fail_silently=False)
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance =request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance =request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance =request.user)
        p_form = ProfileUpdateForm(instance =request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]