from django.shortcuts import render, get_object_or_404
from messages.models import Message, Topic
from messages.forms import MessageForm

import logging

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

def ancestors(request, message_id):
    context = {}
    message = get_object_or_404(Message, pk=message_id)
    context['message_list'] = message.get_ancestors()
    logging.error(context['message_list'])
    return render(request, 'message_list.tmpl', context)

def children(request, message_id):
    context = {}
    message = get_object_or_404(Message, pk=message_id)
    context['message_list'] = message.children.all()
    logging.info(context['message_list'])
    return render(request, 'message_list.tmpl', context)
