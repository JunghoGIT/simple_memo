# Generated by Django 4.0.1 on 2022-02-01 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
        ('memo', '0003_memo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', to_field='nickname'),
        ),
    ]
