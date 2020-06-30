from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product__id=pk)
    form = ReviewForm
    reviewed_products = request.session['reviewed_products'] if 'reviewed_products' in request.session else []

    if request.method == 'POST':
        if product.id not in reviewed_products:
            form = ReviewForm(data=request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.product = product
                new_review.save()
                reviewed_products.append(product.id)
                request.session['reviewed_products'] = reviewed_products

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': True if product.id in reviewed_products else False
    }

    return render(request, template, context)
