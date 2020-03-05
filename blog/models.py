from django.db import models

# Create your models here.
class Admin(models.Model):
    # id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=128)
    blog_title = models.CharField(max_length=60)
    blog_sub_title = models.CharField(max_length=120)
    name = models.CharField(max_length=40)
    about = models.TextField()

class Category(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)


class Post(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    # 与Category表关联
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    # id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=40)
    text = models.TextField()
    from_admin = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True, db_index=True)

    # 与Post表关联
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # 自关联(评论内的评论)
    replied = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)