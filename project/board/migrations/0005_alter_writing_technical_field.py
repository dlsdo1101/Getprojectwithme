# Generated by Django 3.2.13 on 2022-05-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_writing_technical_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writing',
            name='technical_field',
            field=models.CharField(choices=[('other', '기타'), ('game', '게임'), ('ai', '인공지능'), ('web', '웹'), ('앱', 'app')], default='', max_length=80),
        ),
    ]