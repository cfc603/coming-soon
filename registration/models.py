from django.db import models


class Entry(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.email
