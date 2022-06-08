# Generated by Django 4.0.5 on 2022-06-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_log', models.DateTimeField(auto_now=True)),
                ('activity_log', models.CharField(choices=[('Added', 'Added'), ('Deleted', 'Deleted'), ('Update', 'Update')], max_length=200)),
                ('eval_log', models.CharField(choices=[('LMS', 'LMS'), ('HR', 'HR'), ('AIV', 'AIV')], max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
            ],
        ),
    ]
