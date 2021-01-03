from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserregisterForm, UserUpdateForm, ProfileUpdateForm
from tweetapi.models import Tweets
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer



# def home(request):
#     context = {
#         'tweets': Tweets.objects.all()
#     }
#     return render(request, 'users/home.html',context)


def register(request):
    if request.method == 'POST':
        form = UserregisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserregisterForm()
    return render(request, 'users/register.html', {'form':form})


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
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]