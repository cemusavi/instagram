# Generated by Django 3.2.4 on 2021-07-01 23:01

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import lib.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='title')),
                ('email', models.EmailField(blank=True, max_length=150, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=11, verbose_name='phone_number')),
                ('preview_info', models.BooleanField(default=False, verbose_name='preview information')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='location.location')),
            ],
            options={
                'verbose_name': 'Business',
                'verbose_name_plural': 'Business',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(max_length=40, verbose_name='first name')),
                ('last_name', models.CharField(max_length=40, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Determines whether user is active or not', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=lib.functions.rename_profile)),
                ('bio', models.TextField(blank=True)),
                ('website_link', models.URLField(blank=True, max_length=150)),
                ('public_private', models.BooleanField(default=False)),
                ('business', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.business')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
