# Generated by Django 5.1.3 on 2024-11-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_taken', to='main.students', verbose_name='Студенты'),
        ),
        migrations.AlterField(
            model_name='students',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='students_courses', to='main.course', verbose_name='Посещаемые курсы'),
        ),
    ]
