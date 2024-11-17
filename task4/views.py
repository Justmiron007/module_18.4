from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    return render(request, 'fourth_task/shop.html', {
        'manga': ["Наруто", "Блич", "Ван пис"]
    })


def cart(request):
    return render(request, 'fourth_task/cart.html')
