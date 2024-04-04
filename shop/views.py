from django.shortcuts import render, get_object_or_404
from .models import Wine, Category, Region, Country
from cart.forms import CartAddProductForm
# Create your views here.


def wine_list(request,
              category_slug=None,
              country_slug=None,
              region_slug=None):
    try:
        category = None
        categories = Category.objects.all()
        country = None
        countries = Country.objects.all()
        region = None
        regions = Region.objects.all()

        wines = Wine.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            wines = wines.filter(category=category)

        if country_slug:
            country = get_object_or_404(Country, slug=country_slug)
            wines = wines.filter(country=country)

        if region_slug:
            region = get_object_or_404(Region, slug=region_slug)
            wines = wines.filter(region=region)

        return render(request, 'wine/wine_list.html',
                    {'region': region,
                    'regions': regions,
                    'country': country,
                    'countries': countries,
                    'category': category,
                    'categories': categories,
                    'wines': wines}
                    )
    except Exception as e:
        print(e)
        return render(request, 'wine/wine_list.html')


def wine_detail(request, id, slug):
    wine = get_object_or_404(Wine, id=id, slug=slug, available=True)

    return render(request, 'wine/wine_detail.html', {'wine': wine})


def wine_detail(request, id, slug):
    wine = get_object_or_404(Wine, id=id,
                             slug=slug,
                             available=True)
    cart_wine_form = CartAddProductForm()
    return render(request, 'wine/wine_detail.html', {'wine': wine, 'cart_wine_form': cart_wine_form})
