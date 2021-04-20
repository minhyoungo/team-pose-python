# Generated by Django 3.2 on 2021-04-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0003_alter_membermodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortpolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=80)),
                ('sub_title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('participants', models.ManyToManyField(blank=True, to='members.MemberModel')),
            ],
        ),
    ]