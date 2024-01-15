from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Item
from .models import Sale
from .forms import SaleForm, SaleSearchForm
from .utils import get_item_name_by_item_id, get_chart

import pandas as pd
import matplotlib.pyplot as plt



@require_POST
def create_sale_view(request):
    sale_form = SaleForm
    if request.method == "POST":
        item_id = request.POST.get("item_id")
        item = get_object_or_404(Item, id=item_id)
        form = SaleForm(request.POST or None)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.item = item
            item.sold = True
            item.save()
            sale.save()
            return redirect("home")
        
    context = {
        "sale_form": sale_form, 
    }
    return render(request, "core/partials/modal.html", context)


def get_all_sales_view(request):
    sales = Sale.objects.all()
    

    context = {
        "sales": sales
    }
    return render(request, "sales/all_sales.html", context)


def sales_report(request):
    form = SaleSearchForm()
    sales_df = None
    
    if request.method == "POST":
        form = SaleSearchForm(request.POST)
        if form.is_valid():
            date_from = form.cleaned_data.get("date_from")
            date_to = form.cleaned_data.get("date_to")

            sales_qs = Sale.objects.filter(created_at__date__gte=date_from, created_at__date__lte=date_to)
            print(sales_qs)

            sales_df = pd.DataFrame(sales_qs.values())
            sales_df["created_at"] = sales_df["created_at"].apply(lambda x: x.strftime("%Y-%m-%d"))
            sales_df = sales_df.drop("updated_at", axis=1)
            sales_df.columns = sales_df.columns.str.replace("item_id", "item")
            sales_df["item"] = sales_df["item"].apply(get_item_name_by_item_id)

            df = sales_df.groupby("id", as_index=False)['income'].agg("sum")
            
            chart = get_chart("bar", sales_df)

            # chart_type = 'bar'  # lub inny rodzaj wykresu, jaki chcesz użyć
            # results_by = 'income'  # lub inna kolumna, którą chcesz uwzględnić w wykresie
            # chart = get_chart(chart_type, df, results_by, date_from, date_to)


            print(sales_df)

            

            pd.set_option('colheader_justify', 'center')
            sales_df = sales_df.to_html()

    context = {
        "form": form,
        "sales_df": sales_df,
        "chart": chart
    }

    return render(request, "sales/sales_report.html", context)