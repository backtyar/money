# Generated by Django 4.2.7 on 2023-11-21 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0006_alter_usercategory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='my_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.category', verbose_name='Категории пользователя'),
        ),
    ]
