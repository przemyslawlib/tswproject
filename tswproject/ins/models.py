from django.db import models
from pygments.lexers import get_all_lexers

ALL_LANGUAGES = ((item[1][0],item[0]) for item in get_all_lexers())

# Create your models here.
class Instruction(models.Model):
    title = models.CharField(max_length=250)
    introduction = models.TextField()
    
    def __unicode__(self):
        return self.title

class Task(models.Model):
    inst = models.ForeignKey(Instruction)
    title = models.CharField(max_length=250)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title

class Snippet(models.Model):
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=20, choices=ALL_LANGUAGES)
    code = models.TextField()
    
    def __unicode__(self):
        return self.name

