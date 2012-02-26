from django.db import models
from pygments.lexers import get_all_lexers

ALL_LANGUAGES = ((item[1][0],item[0]) for item in get_all_lexers())

# Create your models here.

class Snippet(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=20, choices=ALL_LANGUAGES)
    code = models.TextField()
