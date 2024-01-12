from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Item
from .models import Sale
from .forms import SaleForm



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