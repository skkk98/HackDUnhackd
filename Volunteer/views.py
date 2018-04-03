from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from Ngo.models import Event
from .models import Regevent, Feedback
from .forms import FeedbackForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import datetime
# Create your views here.
"""class profile(TemplateView):
    template_name = 'profile.html'"""


def profile(request):
    user_id = request.user
    find_events = Regevent.objects.get(user=user_id)
    list_events = find_events.events.split('&')
    print(list_events)
    list_events = list_events[:-1]
    all_events = Event.objects.all().exclude(id__in=list_events)
    template_name = 'profile.html'
    return render(request, template_name, {'all_events': all_events})

def event_reg(request, event_id, user_id):
    users = request.user
    findevent = Event.objects.get(pk=event_id)
    findevent.users += str(user_id) + '&'
    findevent.save()
    if Regevent.objects.filter(user=users).exists():
        finduser = Regevent.objects.get(user=users)
        finduser.events += str(event_id) + '&'
        finduser.save()
    else:
        regevent = Regevent(user=users, events=str(event_id) + '&')
        regevent.save()
    message = render_to_string('event_description.html', {

    })
    mail_subject = 'Details Of the Registered Event'
    to_email = users.email
    email = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=[to_email])
    email.attach_file('/home/kalyan/PycharmProjects/HackdUnhackd' + findevent.image.url)
    email.send()
    return HttpResponseRedirect('/volunteer/profile')

def event_unreg(request, event_id, user_id):
    # remove user_id from event
    users = request.user
    findevent = Event.objects.get(pk=event_id)
    oldstr = findevent.users
    k = findevent.users.find(str(user_id))
    print(k)
    l = len(str(user_id))
    newstr = oldstr[0:k] + oldstr[k+l+1:]
    print(oldstr)
    print(newstr)
    findevent.users = newstr
    findevent.save()
    # remove event_id from user's
    finduser = Regevent.objects.get(user=users)
    old = finduser.events
    p = finduser.events.find(str(event_id))
    l1 = len(str(event_id))
    new = old[0:p] + old[p+l1+1:]
    finduser.events = new
    print(p)
    print(old)
    print(new)
    finduser.save()
    return HttpResponseRedirect('/volunteer/profile/regevents')

def regd_events(request):
    template_name = 'regd_events.html'
    user_id = request.user
    find_events = Regevent.objects.get(user=user_id)
    list_events = find_events.events.split('&')
    print(list_events)
    list_events = list_events[:-1]
    events = Event.objects.filter(id__in=list_events)
    return render(request, template_name, {'events': events,
                                                'datetime': datetime.date.today})

def feedback(request, event_id):
    if request.method == 'GET':
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})
    else:
        review = request.POST['review']

        feedback = Feedback()
        findevent = Event.objects.get(pk=event_id)
        feedback.event = findevent
        feedback.review = review

        feedback.save()
        return HttpResponse('Thanks for your feedback')
