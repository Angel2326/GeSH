<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product


# Create your views here.
@login_required
def basket_add(request, product_id=None):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
