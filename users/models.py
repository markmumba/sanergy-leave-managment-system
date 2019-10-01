from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from PIL import Image
from sanergy_leave.models import Role

from sanergy_leave.models import Department


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING,null=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, null=True)
    date_of_birth = models.DateField(default=timezone.now)
    joined_date = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=15, blank=True,null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_employee =  models.BooleanField(default=False, null=True)



    def __str__(self):
      return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
