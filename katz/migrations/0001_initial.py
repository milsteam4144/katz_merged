# Generated by Django 3.2.16 on 2023-04-11 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('breeder_name', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('cattery', models.CharField(blank=True, max_length=60, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('cust_last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('cust_venmo_name', models.CharField(blank=True, max_length=30, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('catID', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=15, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatTest',
            fields=[
                ('name', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('color', models.CharField(blank=True, max_length=15, null=True)),
                ('personality', models.CharField(blank=True, max_length=15, null=True)),
                ('price', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('birthday', models.DateField(null=True)),
                ('breeder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='katz.breeder')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('catType', models.CharField(default='breeder', max_length=10)),
                ('status', models.CharField(default='breeder', max_length=10)),
                ('pattern', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('mother', models.IntegerField(blank=True, null=True)),
                ('father', models.IntegerField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('personality', models.TextField(blank=True, null=True)),
                ('breederId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='katz.breeder')),
            ],
        ),
    ]
