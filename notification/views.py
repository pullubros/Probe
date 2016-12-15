from django.shortcuts import render_to_response
from .models import Notification
from django.http import HttpResponseRedirect


def show_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    return render_to_response('notification.html', {'notification': n})


def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect("/question/all")
