from django.db import models

# Create your models here.
class Html(models.Model):
    title = models.CharField(max_length=246)
    desc = models.CharField(max_length=700, blank=True)
    html = models.FileField(upload_to='show/templates/show/')

    def __str__(self):
        return self.title+' & '+self.html.name