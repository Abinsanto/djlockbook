# from django.shortcuts import render,redirect
# from myapp.forms import customerform
# # Create your views here.
#
# def home(request):
#     if request.method=='POST':
#         myform=customerform(request.POST)
#         if myform.is_valid():
#             myform.save()
#             # return redirect("read")
#         return render(request, 'index1.html')
#     else:
#         myform=customerform
#         return render(request,"index1.html",{'form':myform})

#
# from django.shortcuts import render, redirect
# from .forms import CustomerForm
#
# def home(request):
#     if request.method == 'POST':
#         myform = CustomerForm(request.POST)
#         if myform.is_valid():
#             myform.save()
#             return redirect('home')  # Redirect to the same page after saving
#     else:
#         myform = CustomerForm()
#
#     return render(request, 'index1.html', {'form': myform})




#
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import CustomerForm
# from .models import Customer
#
#
# def signup_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm = request.POST.get('confirm')
#
#         if password != confirm:
#             return render(request, 'signup.html', {'error': 'Passwords do not match!'})
#         elif User.objects.filter(username=username).exists():
#             return render(request, 'signup.html', {'error': 'Username already taken!'})
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             return redirect('login_page')
#
#     return render(request, 'signup.html')
#
#
# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password!'})
#
#     return render(request, 'login.html')
#
#
# def logout_user(request):
#     logout(request)
#     return redirect('login_page')
#
#
# @login_required
# def home(request):
#     if request.method == 'POST':
#         myform = CustomerForm(request.POST)
#         if myform.is_valid():
#             book = myform.save(commit=False)
#             book.user = request.user  # ✅ Link book to current logged-in user
#             book.save()
#             return redirect('home')
#     else:
#         myform = CustomerForm()
#
#     # ✅ Show only current user’s books
#     books = Customer.objects.filter(user=request.user)
#     return render(request, 'index1.html', {'form': myform, 'books': books, 'user': request.user})
#
# @login_required
# def home(request):
#     if request.method == 'POST':
#         myform = CustomerForm(request.POST)
#         if myform.is_valid():
#             book = myform.save(commit=False)
#             book.user = request.user  # attach the logged-in user
#             book.save()
#             return redirect('home')
#     else:
#         myform = CustomerForm()
#
#     # show only that user’s books
#     books = Customer.objects.filter(user=request.user)
#     return render(request, 'index1.html', {'form': myform, 'books': books, 'user': request.user})





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import Customer

def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken!'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login_page')
    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login_page')


@login_required
def home(request):
    if request.method == 'POST':
        myform = CustomerForm(request.POST)
        if myform.is_valid():
            book = myform.save(commit=False)
            book.user = request.user  # assign logged-in user automatically
            book.save()
            return redirect('home')
    else:
        myform = CustomerForm()

    books = Customer.objects.filter(user=request.user)
    return render(request, 'index1.html', {'form': myform, 'books': books, 'user': request.user})


@login_required
def delete_book(request, id):
    book = get_object_or_404(Customer, id=id, user=request.user)
    book.delete()
    return redirect('home')
