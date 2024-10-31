import os
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings


class WorkSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    screenshot_paths = models.JSONField(default=list)  # Ensure this line is present

    def save_screenshot(self, img):
        directory = os.path.join(settings.MEDIA_ROOT, 'screenshots', str(self.id))
        os.makedirs(directory, exist_ok=True)
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(directory, filename)
        img.save(filepath)
        self.screenshots.append(filepath)
        self.save()

    def __str__(self):
        return f"{self.user.username}'s session from {self.start_time}"
