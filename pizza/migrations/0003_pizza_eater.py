# Generated by Django 3.1.1 on 2020-09-16 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0002_auto_20200916_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='eater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
