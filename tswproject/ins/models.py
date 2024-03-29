from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles, get_style_by_name
from pygments.formatters import HtmlFormatter

ALL_LANGUAGES = ((item[1][0],item[0]) for item in get_all_lexers())
ALL_STYLES = (item for item in get_all_styles())

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    def __unicode__(self):
        return self.title

class Instruction(models.Model):
    title = models.CharField(max_length=250)
    introduction = models.TextField()
    subject = models.ForeignKey(Subject)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        permissions = (
            ('view_instruction', 'View Instruction'),
        )

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
    
    def pygmented(self):
        lexer = get_lexer_by_name(self.language, stripall=True)
        formatter = HtmlFormatter(lineos=True, cssclass="source", style='default')
        return highlight(self.code, lexer, formatter)
