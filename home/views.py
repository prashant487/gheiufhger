from django.shortcuts import render

# Create your views here.
from home.models import contactinfo, contact, testm


def homes(request):
    view = {}
    view['reviews'] = testm.objects.all()
    return render(request, 'index.html',view)


def about(request):
    return render(request, 'about.html')


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def price(request):
    return render(request, 'price.html')


def services(request):
    return render(request, 'services.html')


def blog_home(request):
    return render(request, 'blog-home.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    view = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject= subject,
            message = message
        )
        data.save()
        view['success'] = "The message is submitted."

    view['info'] = contactinfo.objects.all()
    return render(request, 'contact.html',view)





