from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)
    comment_required = models.BooleanField(default=False)
    essential = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['date']

    def clean(self):
            if self.category.comment_required and not self.comment:
                raise ValidationError('The comment is required for this category')

    def __unicode__(self):
        return '%s - %s' % (self.category, self.amount)


class ExpenseRegular(models.Model):
    """Monthly Expense"""
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category)
    delayed = models.BooleanField(default=False)
    advanced = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s - %s' % (self.name, self.category, self.amount)


class IncomeRegular(models.Model):
    """Monthly Income"""
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.amount)


class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s - %s' % (self.amount, self.comment)
