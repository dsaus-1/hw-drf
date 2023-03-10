from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='аватар', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    students = models.ManyToManyField(User, verbose_name='ученики', **NULLABLE)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='lesson/', verbose_name='аватар', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='ссылка на видео')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title


