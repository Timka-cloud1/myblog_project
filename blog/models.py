from django.db import models
from django.contrib.auth.models import User

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__isnull=False)

    def by_author(self, author):
        return self.get_queryset().filter(author=author)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    objects = models.Manager()
    published = PublishedPostManager()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='categories')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'



