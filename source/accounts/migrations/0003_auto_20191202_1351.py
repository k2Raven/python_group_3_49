# Generated by Django 2.2.5 on 2019-12-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания работы'),
        ),
        migrations.AlterField(
            model_name='team',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала работы'),
        ),
    ]
