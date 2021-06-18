from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    book_id = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    category_img = models.FileField(upload_to='images/category', default=None)
    categoty_activate = models.BooleanField(default=True)
    category_detail = models.TextField()

    def __str__(self):
        return self.book_id


class bookshop(models.Model):
    book_id = models.CharField(max_length=20, primary_key=True)
    book_slug = models.SlugField(max_length=200, unique=True)
    book_name = models.CharField(max_length=100)
    book_des = models.TextField(max_length=255)
    book_category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    book_img = models.FileField(blank=True)
    book_price = models.FloatField(default=0)
    book_datetime = models.DateTimeField(auto_now=True)
    book_created = models.DateTimeField(auto_now_add=True)
    book_recommend = models.BooleanField(default=True)
    book_active = models.BooleanField(default=True)

    def __str__(self):
        return self.book_id


class PostImage(models.Model):
    post = models.ForeignKey(bookshop, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/product')

    def __str__(self):
        return self.post.book_id


class ImageProfile(models.Model):
    name = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    images = models.FileField(
        upload_to='images/profile', default='images/profile/favicon.png',)

    def __str__(self):
        return self.name.username


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
