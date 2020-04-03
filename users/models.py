from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

LOCATIONS = [
    ('BAR', 'Barisal'),
    ('CHI', 'Chittagong'),
    ('DHK', 'Dhaka'),
    ('KHI', 'Khulna'),
    ('MYM', 'Mymensingh'),
    ('RAJ', 'Rajshahi'),
    ('RAN', 'Rangpur'),
    ('SYL', 'Sylhet')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(choices=LOCATIONS, max_length=5)
    phone = models.CharField(blank=True, max_length=30)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()