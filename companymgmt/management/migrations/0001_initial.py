# Generated by Django 4.0.2 on 2022-02-15 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('postcode', models.CharField(max_length=10)),
                ('logo', models.ImageField(upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('job_position', models.CharField(max_length=30)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='management.company')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=60)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('company', models.ManyToManyField(related_name='bank', to='management.Company')),
            ],
        ),
    ]