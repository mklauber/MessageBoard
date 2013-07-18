from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

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


    def __unicode__(self):
        return "%s%s %s" % (self.pk, "-" + str(self.parent.pk) if self.parent else "", self.text)
