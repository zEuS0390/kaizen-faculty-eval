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
            name='AIVCriterion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AIVRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1st-Sem', 'First Semester'), ('2nd-Sem', 'Second Semester')], default='1st-Sem', max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.member')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.schoolyear')),
            ],
        ),
        migrations.CreateModel(
            name='AIVCriterionScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_visit', models.FloatField(blank=True, null=True)),
                ('second_visit', models.FloatField(blank=True, null=True)),
                ('average_score', models.FloatField(blank=True, null=True)),
                ('remarks', models.CharField(max_length=200)),
                ('aivcriterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aiv.aivcriterion')),
                ('aivrating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aiv.aivrating')),
            ],
        ),
    ]