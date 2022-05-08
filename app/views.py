from django.shortcuts import render, redirect

from app.filters import ContractorFilter
from app.forms import ContractorCreate, OrderCreate, EmployeeCreate, PackingListCreate, ProductCreate, \
    StockProductCreate, GiveawayCreate, SignIn
from app.models import Contractor, Product, Employee, Order, PackingList, StockProduct, Giveaway
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    contractors = ContractorFilter(request.GET, queryset=Contractor.objects.get_table_data())
    return render(request, 'index.html', {
        "contractors": contractors,
    })

@login_required
def index2(request):
    products = Product.objects.get_table_data()

    return render(request, 'index2.html', {
        "products": products,
    })
@login_required
def index3(request):
    employees = Employee.objects.get_table_data()

    return render(request, 'index3.html', {
        "employees": employees,
    })
@login_required
def index4(request):
    orders = Order.objects.get_table_data()

    return render(request, 'index4.html', {
        "orders": orders,
    })
@login_required
def index5(request):
    packing_lists = PackingList.objects.get_table_data()

    return render(request, 'index5.html', {
        "packing_lists": packing_lists,
    })
@login_required
def index6(request):
    stock_products = StockProduct.objects.get_table_data()

    return render(request, 'index6.html', {
        "stock_products": stock_products,
    })
@login_required
def index7(request):
    giveaways = Giveaway.objects.get_table_data()

    return render(request, 'index7.html', {
        "giveaways": giveaways,
    })


def auth(request):
    if request.user.is_authenticated:
        return redirect('/stockproducts')
    if request.method == 'POST':
        form = SignIn(data=request.POST)
        if form.is_valid():

            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/stockproducts')
            return render(request, 'auth.html', {'error_auth': 'Неверный логин или пароль'})
        return render(request, 'auth.html', {'error_auth': 'Неверный логин или пароль'})
    return render(request, 'auth.html', {})
@login_required
def change(request, id):
    if request.method == 'POST':
        instance = Contractor.objects.get(id=id)
        form = ContractorCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/contractors')
    else:
        contractor = Contractor.objects.get(id=id)
        form = ContractorCreate(instance=contractor)
    return render(request, 'add_change.html', {'form': form})
@login_required
def add(request):
    if request.method == 'POST':
        form = ContractorCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contractor/add')
    else:
        form = ContractorCreate()
    return render(request, 'add_change.html', {'form': form})

@login_required
def delete_add_change(request, id):
    Contractor.objects.get(id=id).delete()
    return redirect('/contractors')

@login_required
def change2(request, id):
    if request.method == 'POST':
        instance = Product.objects.get(id=id)
        form = ProductCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        product = Product.objects.get(id=id)
        form = ProductCreate(instance=product)
    return render(request, 'add_change2.html', {'form': form})
@login_required
def add2(request):
    if request.method == 'POST':
        form = ProductCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/add')
    else:
        form = ProductCreate()
    return render(request, 'add_change2.html', {'form': form})

@login_required
def delete_add_change2(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/products')
@login_required
def change3(request, id):
    if request.method == 'POST':
        instance = Employee.objects.get(id=id)
        form = EmployeeCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        employee = Employee.objects.get(id=id)
        form = EmployeeCreate(instance=employee)
    return render(request, 'add_change3.html', {'form': form})
@login_required
def add3(request):
    if request.method == 'POST':
        form = EmployeeCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee/add')
    else:
        form = EmployeeCreate()
    return render(request, 'add_change3.html', {'form': form})

@login_required
def delete_add_change3(request, id):
    Employee.objects.get(id=id).delete()
    return redirect('/employees')

@login_required
def add4(request):
    if request.method == 'POST':
        form = OrderCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order/add')
    else:
        form = OrderCreate()
    return render(request, 'add_change4.html', {'form': form})
@login_required
def change4(request, id):
    if request.method == 'POST':
        instance = Order.objects.get(id=id)
        form = OrderCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/orders')
    else:
        order = Order.objects.get(id=id)
        form = OrderCreate(instance=order)
    return render(request, 'add_change4.html', {'form': form})
@login_required
def delete_add_change4(request, id):
    Order.objects.get(id=id).delete()
    return redirect('/orders')
@login_required
def add5(request):
    if request.method == 'POST':
        form = PackingListCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/packinglist/add')
    else:
        form = PackingListCreate()
    return render(request, 'add_change5.html', {'form': form})
@login_required
def change5(request, id):
    if request.method == 'POST':
        instance = PackingList.objects.get(id=id)
        form = PackingListCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/packinglists')
    else:
        packinglist = PackingList.objects.get(id=id)
        form = PackingListCreate(instance=packinglist)
    return render(request, 'add_change5.html', {'form': form})
@login_required
def delete_add_change5(request, id):
    PackingList.objects.get(id=id).delete()
    return redirect('/packinglists')
@login_required
def add6(request):
    if request.method == 'POST':
        form = StockProductCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stockproduct/add')
    else:
        form = StockProductCreate()
    return render(request, 'add_change6.html', {'form': form})
@login_required
def change6(request, id):
    if request.method == 'POST':
        instance = StockProduct.objects.get(id=id)
        form = StockProductCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/stockproducts')
    else:
        stockproduct = StockProduct.objects.get(id=id)
        form = StockProductCreate(instance=stockproduct)
    return render(request, 'add_change6.html', {'form': form})
@login_required
def delete_add_change6(request, id):
    StockProduct.objects.get(id=id).delete()
    return redirect('/stockproducts')
@login_required
def add7(request):
    if request.method == 'POST':
        form = GiveawayCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/giveaway/add')
    else:
        form = GiveawayCreate()
    return render(request, 'add_change7.html', {'form': form})
@login_required
def change7(request, id):
    if request.method == 'POST':
        instance = Giveaway.objects.get(id=id)
        form = GiveawayCreate(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/giveaways')
    else:
        giveaway = Giveaway.objects.get(id=id)
        form = GiveawayCreate(instance=giveaway)
    return render(request, 'add_change7.html', {'form': form})
@login_required
def delete_add_change7(request, id):
    Giveaway.objects.get(id=id).delete()
    return redirect('/giveaways')

def logoutButton(request):
    logout(request)
    return redirect('/')


