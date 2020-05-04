from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def contact(request):
    if  request.method == "POST":
        listing_id=request.POST["listing_id"]
        listing=request.POST["listing"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        user_id=request.POST["user_id"]
        realtor_email=request.POST["realtor_email"]

        #Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You Have already made inquiry for this listing")

                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        # Send Email
        send_mail(
            'Property Listing Inquiry',
            'There has been a inquiry for '+listing+". Sign into th admin panel for more info",
            'yousufibrahim2003@gmail.com',
            [realtor_email,"dacino2693@katamo1.com"],
            fail_silently=False,
        )

        messages.success(request,"Your request has been submitted , a realtor will get back to you soon")

        return redirect('/listings/'+listing_id)



