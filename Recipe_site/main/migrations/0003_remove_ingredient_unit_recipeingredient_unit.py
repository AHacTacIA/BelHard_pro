# Generated by Django 5.1.3 on 2024-12-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ingredient_options_recipe_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[('кг', 'Килограмм'), ('гр', 'Грамм'), ('мг', 'Миллиграмм'), ('л', 'Литр'), ('мл', 'Миллилитр'), ('стак.', 'Стакан'), ('стол.л.', 'Столовая ложка'), ('чайн.л.', 'Чайная ложка'), ('десертн.л.', 'Десертная ложка'), ('шт.', 'Штука')], default='', max_length=50, verbose_name='Ед.измерения'),
            preserve_default=False,
        ),
    ]