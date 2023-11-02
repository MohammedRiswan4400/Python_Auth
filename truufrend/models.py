from django.db import models
from django.contrib.auth.models import User

class Otp(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)  # Assuming a maximum length for phone numbers, adjust as needed
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)  # Link to your user model

    def __str__(self):
        return self.phone_number
class Profile(models.Model):
    CHOICES = (
        ('Anxiety', 'Anxiety'),
        ('Motivation', 'Motivation'),
        ('Confidence', 'Confidence'),
        ('Sleep', 'Sleep'),
        ('Depression', 'Depression'),
        ('Work Stress', 'Work Stress'),
        ('Relationships', 'Relationships'),
        ('Exam stress', 'Exam stress'),
        ('Pregnancy', 'Pregnancy'),
        ('Loss', 'Loss'),
        ('LGBTQ+', 'LGBTQ+'),
        ('Low Energy', 'Low Energy'),
        ('Self Esteem', 'Self Esteem'),
        ('Loneliness', 'Loneliness'),
        ('Trauma', 'Trauma'),
        ('Health issues', 'Health issues'),
    )
    dp=models.ImageField(upload_to='img/profile_pictures',null=True, blank=True)
    name = models.CharField(max_length=100)
    nick_name=models.CharField(max_length=50)
    choices=(('13-17 years old','13-17 years old'),('18 Years and old','18 Years and old'))
    age = models.IntegerField(null=True, blank=True,choices=choices)
    challenges=models.TextField(choices=CHOICES)

class SOS(models.Model):
    contact=models.CharField(max_length=15, unique=True)
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='media/videos/')











# Create your models here.
