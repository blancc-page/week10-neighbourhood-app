# Generated by Django 4.0.5 on 2022-06-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodApp', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='http://cdn.onlinewebfonts.com/svg/img_364496.png', upload_to='images/'),
        ),
    ]