from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.contrib import messages

from .models import Customer, Product, Supplier, Store, Payment, Report
from .forms import CustomerForm, ProductForm, SupplierForm, StoreForm, PaymentForm, ReportForm


# --- DECORATOR/HELPER CHECKS ---
def is_manager(user):
    """Waxaa lagu tetsiyaa in user-ku yahay Manager (is_staff ama superuser)."""
    return user.is_authenticated and user.is_staff


# --- AUTHENTICATION VIEWS (LOGIN, SIGNUP, LOGOUT) ---

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Marka uu register samaysto, toos profil-kiisa customer loo abuurayo
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email or ''
            )
            login(request, user)
            messages.success(request, "Aad ayaad u mahadsan tahay, diwaan-gelintu waa ku guulaysatay!")
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'sales/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Hadii uu meel kale ka yimid (next param) halkaas u redirect garee, hadii kalana product_list
            next_url = request.GET.get('next', 'product_list')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'sales/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# --- CUSTOMER VIEWS ---

@login_required
def customer_list(request):
    if request.user.is_staff:
        customers = Customer.objects.all()
    else:
        customers = Customer.objects.filter(user=request.user)
    return render(request, 'sales/customer_list.html', {'customers': customers})


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if not request.user.is_staff and customer.user != request.user:
        raise PermissionDenied
    return render(request, 'sales/customer_detail.html', {'customer': customer})


@login_required
@user_passes_test(is_manager)
def customer_create(request):
    form = CustomerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'sales/customer_create.html', {'form': form})


@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if not request.user.is_staff and customer.user != request.user:
        raise PermissionDenied

    form = CustomerForm(request.POST or None, instance=customer)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'sales/customer_update.html', {'customer': customer, 'form': form})


@login_required
@user_passes_test(is_manager)
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'sales/customer_delete.html', {'customer': customer})


# --- PRODUCT VIEWS ---

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sales/product_list.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'sales/product_detail.html', {'product': product})


@login_required
@user_passes_test(is_manager)
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'sales/product_create.html', {'form': form})


@login_required
@user_passes_test(is_manager)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'sales/product_update.html', {'product': product, 'form': form})


@login_required
@user_passes_test(is_manager)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'sales/product_delete.html', {'product': product})


# --- STORE VIEWS (MANAGER ONLY) ---

@login_required
@user_passes_test(is_manager)
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'sales/store_list.html', {'stores': stores})


@login_required
@user_passes_test(is_manager)
def store_create(request):
    form = StoreForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('store_list')
    return render(request, 'sales/store_create.html', {'form': form})


@login_required
@user_passes_test(is_manager)
def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    form = StoreForm(request.POST or None, instance=store)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('store_list')
    return render(request, 'sales/store_update.html', {'store': store, 'form': form})


@login_required
@user_passes_test(is_manager)
def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store_list')
    return render(request, 'sales/store_delete.html', {'store': store})


# --- SUPPLIER VIEWS (MANAGER ONLY) ---

@login_required
@user_passes_test(is_manager)
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'sales/supplier_list.html', {'suppliers': suppliers})


@login_required
@user_passes_test(is_manager)
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'sales/supplier_detail.html', {'supplier': supplier})


@login_required
@user_passes_test(is_manager)
def supplier_create(request):
    form = SupplierForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'sales/supplier_create.html', {'form': form})


@login_required
@user_passes_test(is_manager)
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'sales/supplier_update.html', {'supplier': supplier, 'form': form})


@login_required
@user_passes_test(is_manager)
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'sales/supplier_delete.html', {'supplier': supplier})


# --- PAYMENT VIEWS ---

@login_required
def payment_list(request):
    if request.user.is_staff:
        payments = Payment.objects.all()
    else:
        payments = Payment.objects.filter(customer__user=request.user)
    return render(request, 'sales/payment_list.html', {'payments': payments})


@login_required
def payment_create(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        payment = form.save(commit=False)
        if not request.user.is_staff and hasattr(request.user, 'customer'):
            payment.customer = request.user.customer
        payment.save()
        return redirect('payment_list')
    return render(request, 'sales/payment_create.html', {'form': form})


# --- REPORT VIEWS ---

@login_required
def report_list(request):
    if request.user.is_staff:
        reports = Report.objects.all()
        total_income = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        context = {'reports': reports, 'total_income': total_income, 'is_manager': True}
    else:
        user_payments = Payment.objects.filter(customer__user=request.user)
        total_spent = user_payments.aggregate(Sum('amount'))['amount__sum'] or 0
        context = {'payments': user_payments, 'total_spent': total_spent, 'is_manager': False}

    return render(request, 'sales/report_list.html', context)


@login_required
@user_passes_test(is_manager)
def report_create(request):
    form = ReportForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        report = form.save(commit=False)
        report.created_by = request.user
        report.save()
        return redirect('report_list')
    return render(request, 'sales/report_create.html', {'form': form})