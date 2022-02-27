from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=200, null=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title