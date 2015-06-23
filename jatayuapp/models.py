from django.db import models

# Create your models here.
class SignUp(models.Model):
    full_name = models.CharField(max_length=120, default='', blank=False, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email
