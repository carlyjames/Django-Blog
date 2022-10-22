from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from enum import unique
from operator import mod

from pyexpat import model
import string
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, null = True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    text = RichTextField(null=True,blank=True)
    image = models.FileField(upload_to="photos", null= True, blank= True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)
    category = models.CharField(max_length=200, default= 'Crypto-Currency')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title +  '|' + str(self.author)



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text



class SubscribedUser(models.Model):
    name = models.CharField(max_length=100, null= True)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date Subscribed', default=timezone.now)

    def __str__(self):
        return self.email