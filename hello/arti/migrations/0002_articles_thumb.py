# Generated by Django 2.0.2 on 2018-02-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
