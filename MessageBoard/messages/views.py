from django.shortcuts import render, get_object_or_404
from messages.models import Topic

def index(request):
    context = {}
    context['topics'] = Topic.objects.all()
    return render(request, 'index.html', context)

def topic(request, topic_id):
    context = {}
    topic = get_object_or_404(Topic, pk=topic_id)
    context['topic'] = topic
    context['messages'] = topic.message_set.order_by('created').all()
    return render(request, 'topic.html', context)
