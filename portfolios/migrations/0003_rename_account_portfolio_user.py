# Generated by Django 5.1.4 on 2025-01-15 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_alter_portfolio_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='account',
            new_name='user',
        ),
    ]