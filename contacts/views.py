from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_slug = request.POST['listing_slug']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_slug=listing_slug, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry for that listing')
                return redirect('/listings/'+listing_slug)
            

        contact = Contact(listing=listing, listing_slug=listing_slug, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(

            'LitupRealtors Listing Inquiry',
            'There has been an inquiry for, ' + listing +'. Sign into the admin panel for more details.',
            'lituptech@gmail.com',
            [realtor_email, 'gmndogo@yahoo.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted. A realtor will get back to you soon')
        return redirect('/listings/'+listing_slug)
