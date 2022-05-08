from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} \n {self.content}'


class UserProfile(models.Model):
    author = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='images/profile_pictures', blank=True, null=True)
    facebook_url = models.CharField(max_length=300, blank=True, null=True)
    instagram_url = models.CharField(max_length=300, blank=True, null=True)
    linkedin_url = models.CharField(max_length=300, blank=True, null=True)
    # phoneNumber = models.PhoneNumberField()

    def __str__(self):
        return f'{self.author} /n {self.bio}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.author} /n {self.comment_content}'
