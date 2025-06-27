from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class OTPToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255)
    token = models.CharField(max_length=50)
    expires_at = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        return super().save(*args, **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    @property
    def is_valid(self):
        return not self.is_expired()