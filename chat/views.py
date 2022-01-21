from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from notifications.signals import notify


def chat_send(request):
    try:
        users = User.objects.all()
        print(request.user)
        user = User.objects.get(username=request.user)
        return render(request, 'chat.html', {'users': users, 'user': user})
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages from this view")


def message(request):
    try:
        if request.method == 'POST':
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(id=request.POST.get('user_id'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('chat')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")

def was_read(request):
    request.user.notifications.mark_all_as_read()
    return redirect('chat')
