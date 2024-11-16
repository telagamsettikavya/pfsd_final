# Generated by Django 5.0.2 on 2024-02-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0012_alter_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('aboutus', models.TextField()),
                ('email', models.EmailField(max_length=200)),
                ('mobilenumber', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
