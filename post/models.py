from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    video = models.FileField(upload_to='media/files', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
  
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)

class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)