# Generated by Django 4.0.1 on 2022-01-29 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
