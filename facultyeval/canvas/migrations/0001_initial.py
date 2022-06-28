# Generated by Django 4.0.5 on 2022-06-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_title', models.CharField(choices=[('MG1', 'Modular Group 1'), ('MG2', 'Modular Group 2'), ('MG3', 'Modular Group 3'), ('MG4', 'Modular Group 4')], default='MG1', max_length=200)),
                ('semester', models.CharField(choices=[('1st-Sem', 'First Semester'), ('2nd-Sem', 'Second Semester')], default='1st-Sem', max_length=200)),
                ('part1', models.FloatField()),
                ('part2', models.FloatField()),
                ('final', models.FloatField()),
                ('remarks', models.CharField(max_length=400)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.schoolyear')),
            ],
        ),
    ]