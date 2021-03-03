from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogPost
from .forms import ContactForm

def home_page(request):
    qs = BlogPost.objects.all()[:5]
    content = {'title': 'Welcome to Try Django Blog', 'blog_list':qs}
    return render(request, 'home.html', content)

def about_page(request):
    return render(request, 'about.html', {'title': 'About us'})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        'title': 'Contact us',
        'form': form}
    return render(request, 'form.html', context)