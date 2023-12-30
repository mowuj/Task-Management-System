# Generated by Django 4.2 on 2023-12-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=50)),
                ('task_description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
