# from django.shortcuts import render
#
# def index(request):
#     return render(request, 'blog/index.html')
#

from django.shortcuts import render
from itertools import groupby

def index(request):
    products = [
        {'name': 'Пицца Маргарита', 'category': 'Еда'},
        {'name': 'Бургер', 'category': 'Еда'},
        {'name': 'Футболка', 'category': 'Одежда'},
        {'name': 'Джинсы', 'category': 'Одежда'},
        {'name': 'Ноутбук', 'category': 'Электроника'},
    ]


    products = sorted(products, key=lambda p: p['category'])

    grouped_products = []
    for category, group in groupby(products, key=lambda p: p['category']):
        grouped_products.append({
            'category_name': category,
            'items': list(group)
        })

    return render(request, 'blog/index.html', {'groups': grouped_products})