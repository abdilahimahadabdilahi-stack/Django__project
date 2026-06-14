from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Product, Supplier
from.forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }

    return render(request, 'sales/customer_list.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    context = {
        'customer': customer
    }

    return render(request, 'sales/customer_detail.html', context)


def customer_create(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    context = {
        'form' : form
    }
    return render(request, 'sales/customer_create.html', context)


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST , instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    context = {
        'customer': customer,
        'form': form 
    }

    return render(request, 'sales/customer_update.html', context)


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    context = {
        'customer': customer
    }

    return render(request, 'sales/customer_delete.html', context)




def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'sales/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product
    }

    return render(request, 'sales/product_detail.html', context)


def product_create(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            selling_price=request.POST.get('selling_price'),
            buying_price=request.POST.get('buying_price'),
            category=request.POST.get('category')
        )

        return redirect('product_list')

    context = {}

    return render(request, 'sales/product_create.html', context)


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.selling_price = request.POST.get('selling_price')
        product.buying_price = request.POST.get('buying_price')
        product.category = request.POST.get('category')
        product.save()

        return redirect('product_list')

    context = {
        'product': product
    }

    return render(request, 'sales/product_update.html', context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    context = {
        'product': product
    }

    return render(request, 'sales/product_delete.html', context)


def supplier_list(request):
    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers
    }

    return render(request, 'sales/supplier_list.html', context)


def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    context = {
        'supplier': supplier
    }

    return render(request, 'sales/supplier_detail.html', context)


def supplier_create(request):
    if request.method == 'POST':
        Supplier.objects.create(
            sales_person=request.POST.get('sales_person'),
            address=request.POST.get('address'),
            product=request.POST.get('product'),
            phone=request.POST.get('phone')
        )

        return redirect('supplier_list')

    context = {}

    return render(request, 'sales/supplier_create.html', context)


def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        supplier.sales_person = request.POST.get('sales_person')
        supplier.address = request.POST.get('address')
        supplier.product = request.POST.get('product')
        supplier.phone = request.POST.get('phone')
        supplier.save()

        return redirect('supplier_list')

    context = {
        'supplier': supplier
    }

    return render(request, 'sales/supplier_update.html', context)


def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')

    context = {
        'supplier': supplier
    }

    return render(request, 'sales/supplier_delete.html', context)