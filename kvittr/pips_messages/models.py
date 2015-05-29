from django.db import models
from django.contrib.auth.models import User

class Pip(models.Model):
    pip = models.TextField()
    created_datetime = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name="created_pip")
    likes = models.PositiveIntegerField(default=0)  

    def __unicode__(self):
        return u'%s' % self.pip
    #How the messages (pips) is ordered.
    class Meta:
        ordering = ['-id']