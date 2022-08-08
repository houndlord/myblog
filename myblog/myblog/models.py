from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    publish_date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['by_date']  

    def __str__(self):
        return self.body
