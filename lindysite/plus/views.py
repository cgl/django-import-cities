from django.shortcuts import render
from plus.models import Event

def events_list(request):
    events = Event.objects.filter(is_published=True).order_by('start_date')
    #return render(request, 'plus/events_list.html', {'events': events})
    return render(request, 'plus/index2.html', {'events': events})
