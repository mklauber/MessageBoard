from django.shortcuts import render, get_object_or_404
from messages.models import Message, Topic
from messages.forms import MessageForm

def index(request):
    """List available topics.  A placeholder for navigation to various topics."""
    context = {}
    context['topics'] = Topic.objects.all()
    return render(request, 'index.html', context)

def topic(request, topic_id):
    """Display the messages in a given topic"""
    context = {}
    topic = get_object_or_404(Topic, pk=topic_id)
    context['topic'] = topic
    context['messages'] = topic.message_set.order_by('created').all()
    context['reply_form'] = MessageForm()
    return render(request, 'topic.html', context)
