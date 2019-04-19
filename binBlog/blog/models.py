from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        db_table = 'tag'
    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField('标题', max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField('创建日期')
    update_time = models.DateTimeField('更新日期')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    views = models.PositiveIntegerField(default=0)
    is_show = models.BooleanField(default=1)
    class Meta:
        db_table = 'blog'
        verbose_name_plural = verbose_name = '文章'
        ordering = ['-created_time']
    def __str__(self):
        return self.title
