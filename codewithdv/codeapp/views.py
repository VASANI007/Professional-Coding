# views.py
from multiprocessing import context
from django.shortcuts import render, redirect

from codeproject import settings
from .models import *
from django.core.mail import send_mail
from django.contrib import messages

def indexpage(request):
    cat = category.objects.all()
    context = {
        "category": cat
    }
    return render(request,"index.html", context)

def singlepage(request, id):
    single = ourgallery.objects.get(id=id)
    context ={
        "data": single
    }
    return render(request, "single.html", context)


def contactpage(request):
    if request.method == "POST":
        cname = request.POST.get("name")
        cemail = request.POST.get("email")
        csubject = request.POST.get("subject")
        cmsg = request.POST.get("message")

        # Save to DB
        contact.objects.create(
            name=cname,
            email=cemail,
            subject=csubject,
            msg=cmsg
        )

        # Send Email
        try:
            send_mail(
                subject="Thank You for Contacting Us!",
                message=f"Dear {cname},\n\nThank you for contacting us. We have received your message and will reply within 24 hours.\n\nRegards,\nProfessional Coding Team",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[cemail],
                fail_silently=False,
            )
            messages.success(request, " Your message has been sent! Check your email.")
        except Exception as e:
            messages.error(request, f" Error sending email: {e}")

        return redirect("/")  # Redirect to the contact page

    return render(request, "contact.html")




def ourgallerypage(request):
    overgallerys = ourgallery.objects.all()
    cat = category.objects.all()
    context = {
        "over" : overgallerys,
        "category": cat
    }
    return render(request,"ourgallery.html", context)


def categorypage(request, id):
    overgallerys = ourgallery.objects.filter(c_id=id)
    cat = category.objects.all()
    context = {
        "over" : overgallerys,
        "category": cat
    }
    return render(request, "category.html", context)

def aboutpage(request):
    return render(request, "about.html")