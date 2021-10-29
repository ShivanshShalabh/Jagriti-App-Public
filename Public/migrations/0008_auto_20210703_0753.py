# Generated by Django 3.2.4 on 2021-07-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Public', '0007_auto_20210703_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_user',
            name='address1',
            field=models.CharField(default='', max_length=125),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='address2',
            field=models.CharField(default='', max_length=125),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='city',
            field=models.CharField(default='', max_length=75),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='state',
            field=models.CharField(default='', max_length=125),
        ),
        migrations.AlterField(
            model_name='app_user',
            name='user_type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
