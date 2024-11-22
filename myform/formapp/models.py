from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='contacts/', null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
