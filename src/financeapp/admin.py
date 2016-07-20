from django.contrib import admin

from daterange_filter.filter import DateRangeFilter

from .models import Category, Expense, ExpenseRegular, IncomeRegular, Income


class ExpenseAdmin(admin.ModelAdmin):
    list_filter = ('category', ('date', DateRangeFilter),)
    list_display = ('date', 'amount', 'category', 'comment')


class ExpenseRegularAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'category', 'delayed', 'advanced')

admin.site.register(Category)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseRegular, ExpenseRegularAdmin)
admin.site.register(IncomeRegular)
admin.site.register(Income)
