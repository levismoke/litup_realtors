from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, county_choices

from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    #get Recommend
    mvp_listings = Listing.objects.order_by('-list_date').filter(recommend=True)[:4]

    #get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'listings': listings,
        'mvp_listings': mvp_listings,
        'mvp_realtors': mvp_realtors,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def contacts(request):
    return render(request, 'pages/contacts.html')