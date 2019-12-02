from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    about_me = models.TextField(max_length=3000, null=True, blank=True, verbose_name='О себе')
    git_http = models.URLField(null=True, blank=True, verbose_name='Профиль на гитхаб')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Team(models.Model):
    user = models.ForeignKey(User, related_name='team', on_delete=models.CASCADE, verbose_name='Пользователь')
    project = models.ForeignKey('webapp.Project', related_name='team', on_delete=models.CASCADE, verbose_name='Проект')
    start_date = models.DateField(verbose_name='Дата начала работы', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Дата окончания работы', null=True, blank=True)
