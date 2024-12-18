# Generated by Django 5.1.3 on 2024-11-27 12:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('c', 'C++'), ('an', 'Android')], max_length=20)),
                ('course_num', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Номер курса')),
                ('start_date', models.DateField(null=True, verbose_name='Начало курса')),
                ('end_date', models.DateField(null=True, verbose_name='Окончание курса')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'db_table': 'courses',
                'ordering': ['name', 'course_num'],
                'unique_together': {('name', 'course_num')},
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Студент')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('sex', models.CharField(choices=[('m', 'Мужчина'), ('w', 'Женщина')], max_length=10, verbose_name='Пол')),
                ('active', models.BooleanField(verbose_name='Активный')),
                ('age', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)])),
                ('course', models.ManyToManyField(blank=True, to='main.course', verbose_name='Посещаемые курсы')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'students',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Оценка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.students')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
                'db_table': 'marks',
            },
        ),
        migrations.AddIndex(
            model_name='students',
            index=models.Index(fields=['surname'], name='students_surname_bf4929_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='students',
            unique_together={('name', 'surname')},
        ),
    ]
