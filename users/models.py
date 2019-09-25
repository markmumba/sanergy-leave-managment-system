from PIL import Image
from django.db import models
from django.utils import timezone
# from department.models import Department
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, related_name='lms_department',
    #                                default=1)
    leave_issuer = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name='leave_issuer',
                                     default=1)
    date_of_birth = models.DateField(default=timezone.now)
    joined_date = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=15, blank=True)
    sick_leave = models.FloatField(default=7)
    annual_leave = models.FloatField(default=12)
    compensation_leave = models.FloatField(default=0)
    fcm_token = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

