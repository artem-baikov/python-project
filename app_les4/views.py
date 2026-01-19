from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import AdvertisementForm
from .models import Advertisement
from django.contrib.auth.decorators import login_required


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_les4/index.html', context)

def top_sellers(request):
    return render(request, 'app_les4/top-sellers.html')

def advertisement(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_les4/advertisement.html', context)

def advertisement_detail(request, pk):
    adv = Advertisement.objects.get(id=pk)
    context = {'advertisement': adv}
    return render(request, 'app_les4/advertisement-detail.html', context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_les4/advertisement-post.html', context)