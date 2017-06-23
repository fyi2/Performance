from django.db import models
from django.core.urlresolvers import reverse
from acct.models import User



class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text_tag = models.CharField(max_length=500, default="tag", blank=True)
    text = models.TextField()
    slug = models.SlugField()
    htmltext = models.TextField(editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Note: "+self.title
    def __str__(self):
        return "Note: "+self.title

class Tag(models.Model):
    user = models.ForeignKey(User)
    user_tag = models.CharField(max_length=25)

    def __unicode__(self):
        return self.user_tag

    def __str__(self):
        return self.user_tag
