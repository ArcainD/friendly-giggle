from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


STATIONS_LIST = []

with open(BUS_STATION_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        temp = {
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District'],
        }
        STATIONS_LIST.append(temp)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(STATIONS_LIST, 10)
    num_page = int(request.GET.get('page', 1))
    stations = paginator.get_page(num_page).object_list
    page = paginator.page(num_page)
    context = {
        'bus_stations': stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
