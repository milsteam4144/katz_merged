# Generated by Django 3.2.16 on 2023-04-11 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katz', '0002_remove_cattest_breeder'),
    ]

    operations = [
        migrations.AddField(
            model_name='cattest',
            name='breeder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='katz.breeder'),
        ),
    ]