from django.shortcuts import render


# Create your views here.
# def index(request):
#     return render(request, 'mainapp/index.html')


def index(request):
    index_context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', index_context)


# def products(request):
#     return render(request, 'mainapp/products.html')


def products(request):
    products_context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00,
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'pic': 'static/vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00,
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'pic': 'static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00,
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'pic': 'static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00, 'description': 'Плотная ткань. Легкий материал.',
             'pic': 'static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00,
             'description': 'Гладкий кожаный верх. Натуральный материал.',
             'pic': 'static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00,
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'pic': 'static/vendor/img/products/Black-Dr-Martens-shoes.png'
             },
        ]
    }
    return render(request, 'mainapp/products.html', products_context)
