from django.shortcuts import render


def home(request):
    return render(request, 'third_task/home.html')


def shop(request):
    items = {
        'item1': 'Наруто',
        'item2': 'Блич',
        'item3': '7 смертных грехов',
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
