from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField('标题', max_length=256)

    content = models.TextField('内容', blank=True)

    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    last_modify_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        ordering = ['-created_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
