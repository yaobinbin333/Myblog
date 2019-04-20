from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
#     ·DateField.auto_now
#     ·每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
# ·DateField.auto_now_add当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    update_time = models.DateTimeField('更新日期', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    views = models.PositiveIntegerField(default=0)
    is_show = models.BooleanField(default=1)
    class Meta:
        db_table = 'blog'
        ordering = ['-created_time']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
