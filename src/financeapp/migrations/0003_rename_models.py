from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0002_auto_20160719_0534'),
    ]

    operations = [
        migrations.RenameModel('RegularExpense', 'ExpenseRegular'),
        migrations.RenameModel('RegularIncome', 'IncomeRegular'),
    ]
