from django.shortcuts import render, redirect, get_object_or_404
from .models import Area, Department1, Group, Department2, Directorate, Bid, Type
from .forms import ReportForm, BidForm
from django.contrib.auth.models import User
from .utils import paginate_area, search_area
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.db.models import Q  # для поиска
import requests


def centre(request):  # о центре
    department1 = Department1.objects.all()
    department2 = Department2.objects.all()
    directorate = Directorate.objects.all()
    group = Group.objects.all()

    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/e254c358e96d1c5506a49b8a/latest/USD'

    response = requests.get(url)
    data = response.json()
    price_rub = data['conversion_rates']['RUB']
    time_oil = data['time_last_update_utc']

    # print(data['conversion_rates']['RUB'])
    # print(data['time_next_update_utc'])

    context = {
        'department1': department1,
        'department2': department2,
        'group': group,
        'directorate': directorate,
        'price_rub': price_rub,
        'time_oil': time_oil,
    }

    return render(request, 'centre/info.html', context)


def licea_area(request):  # Лицензионные участки, поиск
    license_area, search_query = search_area(request)
    custom_range, license_area = paginate_area(request, license_area, 24)
    context = {
        'area': license_area,
        'custom_range': custom_range,
        'search_query': search_query,
    }
    return render(request, 'centre/licea_area.html', context)


def area(request, pk):  # страница конкретного ЛУ
    licenses = Area.objects.get(id=pk)
    context = {
        'licenses': licenses,
    }

    return render(request, 'centre/area.html', context)


def old_doc(request):  # библиотека
    return render(request, 'centre/biblioteka.html')


@login_required(login_url="login")
def create_report(request):  # создать отчет
    form = ReportForm()

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centre')

    context = {'form': form}
    return render(request, 'centre/form-report.html', context)


@login_required(login_url="login")
def create_bid(request):  # подать заявку
    form = BidForm()

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            # form.user = request.user
            form.save()
            return redirect('current_bid')

    context = {'form': form}
    return render(request, 'centre/create_bid.html', context)


@login_required(login_url="login")
def current_bid(request):  # актуальные заявки
    # bids = Bid.objects.filter(user=request.user, date_completed__isnull=True)
    # bids = Bid.objects.filter(date_completed__isnull=True)
    bids = Bid.objects.filter(name=2, date_completed__isnull=True)
    bids_2 = Bid.objects.filter(name=1, date_completed__isnull=True)
    # count = len(bids) + len(bids_2)
    count = len(bids)
    count_2 = len(bids_2)
    context = {
        'bids': bids,
        'bids_2': bids_2,
        'count': count,
        'count_2': count_2,
    }

    return render(request, 'centre/current_bid.html', context)


@login_required(login_url="login")
def viewbid(request, bid_pk):  # редактировать заявку
    bid = get_object_or_404(Bid, pk=bid_pk)
    # bidd = Bid.objects.get(user=bid)
    # print("Вывод заявки", bid.user)
    if request.method == 'GET':
        form = BidForm(instance=bid)
        return render(request, 'centre/viewbid.html', {'bid': bid, 'form': form, 'bidd': bid.user})
    else:
        try:
            form = BidForm(request.POST, instance=bid)
            form.save()
            # return redirect('current_bid')
            return render(request, 'centre/viewbid.html', {
                'bid': bid,
                'form': form,
                'bidd': bid.user
            })
        except ValueError:
            return render(request, 'centre/viewbid.html', {
                'bid': bid,
                'form': form,
                'error': 'Неверные данные'
            })


@login_required(login_url="login")
def completebid(request, bid_pk):  # отметка о выполнении
    # bid = get_object_or_404(Bid, pk=bid_pk)
    bid = get_object_or_404(Bid, pk=bid_pk, user=request.user)

    if request.method == 'POST':
        bid.date_completed = timezone.now()
        bid.save()
        return redirect('current_bid')


@login_required(login_url="login")
def deletebid(request, bid_pk):  # удаление заявки
    bid = get_object_or_404(Bid, pk=bid_pk)
    # bid = get_object_or_404(Bid, pk=bid_pk, user=request.user)
    if request.method == 'POST':
        bid.delete()
        return redirect('current_bid')


@login_required(login_url="login")
def completedbid(request):  # страница выполненных заявок
    # bids = Bid.objects.all().filter(date_completed__isnull=False).order_by('-date_completed')
    bids = Bid.objects.all().filter(name=2, date_completed__isnull=False).order_by('-date_completed')
    bids_2 = Bid.objects.all().filter(name=1, date_completed__isnull=False).order_by('-date_completed')
    count = len(bids)
    count_2 = len(bids_2)
    count_off = count + count_2
    context = {
        'bids': bids,
        'bids_2': bids_2,
        'count': count,
        'count_2': count_2,
        'count_off': count_off,
    }
    return render(request, 'centre/completedbid.html', context)

# def oil(request):
#     url = 'https://api.oilpriceapi.com/v1/prices/latest'
#     headers = {
#         'Authorization': 'Token XXXXXXXXXXXXXXX',
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.get(url=url, headers=headers)
#     data = response.json()
#     print(data)
#     #
#     # url = 'https://api.oilpriceapi.com/v1/prices/latest'
#     # headers = {
#     #     'Authorization': 'Token YOUR_API_KEY',
#     #     'Content-Type': 'application/json'
#     # }
#     #
#     # response = requests.get(url=url, headers=headers)
#     # data = response.json()
#     cur = data['data']['price']
#     context = {
#         'cur': cur
#     }
#     print(data['status'])
#     print(data['data']['price'])
#
#     return render(request, 'centre/info.html', context)
