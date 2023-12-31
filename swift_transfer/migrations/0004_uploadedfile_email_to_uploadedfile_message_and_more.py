# Generated by Django 4.2.6 on 2023-11-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swift_transfer', '0003_remove_uploadedfile_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='email_to',
            field=models.EmailField(default='Send to', max_length=254),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='message',
            field=models.TextField(default='Message'),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='title',
            field=models.CharField(default='Title', max_length=255),
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='your_email',
            field=models.EmailField(default='Your email', max_length=254),
        ),
    ]
