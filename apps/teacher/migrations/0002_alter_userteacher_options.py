# Generated by Django 4.0.6 on 2022-07-31 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userteacher',
            options={'verbose_name': 'Tacher', 'verbose_name_plural': 'Tachers'},
        ),
    ]