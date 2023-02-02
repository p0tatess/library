from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm,booksForm,turnBooks
from .models import booksModel
from datetime import date



def base(request):
    return render(request, 'books/base.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'books/register.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'books/register.html',{'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('base')
                else:
                    return HttpResponse('Неактивный аккаунт')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()

    return render(request, 'books/login.html', {'form':form})

def search_books(request):
    error_message = ''
    if  request.method == 'POST':
         form = booksForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             if cd['days'] <= 30:
                new_post = form.save(commit=False)
                new_post.name = request.user
                new_post.save()
                print('asdasdasdasd')
             else:
                 error_message = 'Нельзя брать книгу больше чем на 30 дней'

    else:
        form = booksForm()
    return render(request, 'books/books.html', {'form': form, 'error_message':error_message})

# def turn_books(request):
#     data = []
#     if booksModel.objects.filter(name=request.user):
#         for i in booksModel.objects.filter(name=request.user):
#             data.append(i.book)
#
#     return render(request,'books/turn_book.html',{'data':data})

def turn_books(request):
    have_books = []
    message = ''
    money = ''
    deadline = ''
    for i in booksModel.objects.filter(name=request.user):
        have_books.append(i.book)


    form = turnBooks(request.POST)

    if request.method == 'POST':
        try:
            if form.is_valid():
                cd = form.cleaned_data
                need_days = booksModel.objects.filter(name=request.user).filter(book=cd['choice_book']).get()
                date_today = date.today()
                date_take_book = need_days.data
                days_take_book = need_days.days
                # deadline = date(2024, 5, 22)
                money = date_today.day - date_take_book.day
                # print(type(date_today.day))
                # print(date_take_book)
                # print(money)
                if money <= days_take_book:
                    message = 'Вы принесли книгу вовремя'
                else:
                    message = f'Вы не успели в срок, заплатите  {money*10} рублей'

                booksModel.objects.filter(name=request.user).filter(book=cd['choice_book']).delete()
        except:
            have_books = 'нет'

    context = {'form':form,'have_books': have_books, 'message':message,'money':money, 'deadline': deadline}

    return render(request, 'books/turn_book.html',context)
