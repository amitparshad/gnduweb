from django.db import models

class event(models.Model):
    name = models.CharField(max_length=100)
    detail=models.TextField()
    image=models.FileField(null=True,blank=True,upload_to="static/events/images")
    def __str__(self):
        return self.name
