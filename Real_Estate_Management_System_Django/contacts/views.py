from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        try:
            email_message = f"Hi,\n\nThere has been an inquiry for {listing} from {name}. Their contact details are as follows:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {message}\n\nPlease sign in to the admin panel for more information."

            send_mail(
                'Property Listing Inquiry',
                email_message,
                'realestate@gmail.com',
                [realtor_email],
                fail_silently=False
            )
            return HttpResponseRedirect('/listings/' + listing_id + '?inquiry=success')
        except BadHeaderError as e:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            return HttpResponse('There was an error sending the email. Please try again later.')

    return HttpResponseRedirect('/listings/' + listing_id)