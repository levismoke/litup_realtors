from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, county_choices

from . models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_slug):
    listing = get_object_or_404(Listing, slug=listing_slug)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # City
    if 'town' in request.GET:
        town = request.GET['town']
        if town:
            queryset_list = queryset_list.filter(town__iexact=town)

    # County
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices,
        'listings': queryset_list,
        'values': request.GET
        
    }
    return render(request, 'listings/search.html', context)