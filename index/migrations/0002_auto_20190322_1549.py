# Generated by Django 2.2rc1 on 2019-03-22 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='help_me',
            field=models.TextField(default='Help me'),
        ),
        migrations.AlterField(
            model_name='question',
            name='original',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='index.Question'),
        ),
    ]