from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Test for post
    if request.POST.get('action') == 'post':

        # Get stuff
        product_id = int(request.POST.get('product_id'))

        #Look up products in the database
        product = get_object_or_404(Product, id=product_id)

        # save to our session
        cart.add(product=product)

        # Return response
        response = JsonResponse({'product Name: ': product.name})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
