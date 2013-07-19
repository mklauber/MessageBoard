from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
import json

class Topic(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s-%s" % (self.pk, self.title)

class Message(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    @property
    def json(self):
        data = {
            'user': self.user.pk,
            'created': self.created.strftime("%Y-%m-%d %H:%M"),
            'text': self.text
        }
        return data

    def __unicode__(self):
        return "%s%s '%s'" % (self.pk, "-" + str(self.parent.pk) if self.parent else "", self.text)
