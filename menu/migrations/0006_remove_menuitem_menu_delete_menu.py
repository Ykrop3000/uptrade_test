# Generated by Django 4.2.6 on 2023-10-12 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menuitem_menu_alter_menuitem_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
