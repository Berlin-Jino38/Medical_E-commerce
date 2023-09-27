# Generated by Django 4.2.4 on 2023-09-01 07:32

from django.db import migrations, models
import myApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=myApp.models.getfileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]