from datetime import date
from dateutil.relativedelta import relativedelta

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django
from django.db.models import Sum

from annoying.decorators import render_to

from .models import Expense, IncomeRegular, ExpenseRegular


@render_to('report.html')
@login_required
def report(request, year, month):
    def get_total_essential_expenses():
        expenses_daily_essential = daily_expenses.filter(category__essential=True).aggregate(total=Sum('amount'))['total']
        expenses_regular_essential = ExpenseRegular.objects.filter(category__essential=True).aggregate(
            total=Sum('amount'))['total']
        return expenses_daily_essential + expenses_regular_essential

    start_date = date(int(year), int(month), 1)
    end_date = start_date + relativedelta(months=1) - relativedelta(days=1)
    daily_expenses = Expense.objects.filter(date__gte=start_date, date__lte=end_date)
    expenses = (daily_expenses.values('category__pk', 'category__name')
                              .annotate(sum=Sum('amount'))
                              .order_by('-sum'))
    total_income = IncomeRegular.objects.aggregate(total=Sum('amount'))['total']
    total_daily_expenses = expenses.aggregate(total=Sum('sum'))['total']
    regular_expenses = (ExpenseRegular.objects.values('category__name')
                                      .annotate(sum=Sum('amount'))
                                      .order_by('-sum'))
    total_real_regular_expenses = regular_expenses.aggregate(total=Sum('sum'))['total']
    total_temp_regular_expenses = ExpenseRegular.objects.exclude(delayed=True).exclude(advanced=True).aggregate(
        total=Sum('amount'))['total']
    total_expenses = total_daily_expenses + total_real_regular_expenses
    total_expenses_essential = get_total_essential_expenses()
    total_expenses_other = total_expenses - total_expenses_essential

    income_minus_essentials = total_income - total_expenses_essential
    other_expenses_percentage = round(total_expenses_other / income_minus_essentials, 2)

    result_real = total_income - total_expenses
    result_temp = total_income - total_daily_expenses - total_temp_regular_expenses
    return {'expenses': expenses, 'start_date': start_date, 'end_date': end_date, 'total_income': total_income,
            'regular_expenses': regular_expenses, 'total_expenses': total_expenses, 'result_real': result_real,
            'result_temp': result_temp, 'essential_expenses': total_expenses_essential,
            'other_expenses': total_expenses_other, 'income_minus_essentials': income_minus_essentials,
            'other_expenses_percentage': other_expenses_percentage}


@render_to('home.html')
@login_required
def home(request):
    today = date.today()
    return redirect('report', today.year, today.month)


def logout(request):
    logout_django(request)
    return redirect('login')
