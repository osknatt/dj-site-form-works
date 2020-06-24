from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

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
    print(request.session.get('is_review_exist'))
    form = ReviewForm

    if request.method == 'POST' and request.session.get('is_review_exist') != True:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.save()
            request.session['is_review_exist'] = True



    context = {
        'form': form,
        'product': product,
        'reviews' : reviews,
        'is_review_exist': request.session.get('is_review_exist')
    }

    return render(request, template, context)
