# Generated by Django 2.2.16 on 2022-03-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220311_2240'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='Вы уже оставили отзыв',
        ),
    ]