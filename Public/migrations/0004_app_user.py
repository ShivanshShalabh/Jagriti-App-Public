# Generated by Django 3.2.4 on 2021-07-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Public', '0003_delete_app_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]