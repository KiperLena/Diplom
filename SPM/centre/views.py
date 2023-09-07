from django.shortcuts import render, redirect, get_object_or_404
from .models import Area, Department1, Group, Department2, Directorate, Bid, Type
from .forms import ReportForm, BidForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

def centre(request):
    department1 = Department1.objects.all()
    department2 = Department2.objects.all()
    directorate = Directorate.objects.all()
    group = Group.objects.all()
    context = {
        'department1': department1,
        'department2': department2,
        'group':  group,
        'directorate': directorate,
    }
    return render(request, 'centre/info.html', context)


def licea_area(request):
    license_area = Area.objects.all()
    paginator = Paginator(license_area, 24)
    page = request.GET.get('page')

    try:
        license_area = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        license_area = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        license_area = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'area': license_area,
        'paginator': paginator,
    }
    return render(request, 'centre/licea_area.html', context)


def area(request, pk):

    licenses = Area.objects.get(id=pk)
    context = {
        'licenses': licenses,
    }

    return render(request, 'centre/area.html', context)


def old_doc(request):
    return render(request, 'centre/biblioteka.html')

@login_required(login_url="login")
def create_report(request):
    form = ReportForm()

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centre')

    context = {'form': form}
    return render(request, 'centre/form-report.html', context)


@login_required(login_url="login")
def create_bid(request):
    if request.method == "GET":
        return render(request, 'centre/create_bid.html', {'form': BidForm()})
    else:
        try:
            form = BidForm(request.POST)
            new_bid = form.save(commit=False)
            new_bid.user = request.user
            new_bid.save()
            return redirect('current_bid')
        except ValueError:
            return render(request, 'centre/create_bid.html', {
                              'form': BidForm(),
                              'error': 'Переданы не верные данные. Попробуйте еще раз!',
                          })

@login_required(login_url="login")
def current_bid(request):
    # bids = Bid.objects.filter(user=request.user, date_completed__isnull=True)
    bids = Bid.objects.all()
    context = {
        'bids': bids,
    }
    return render(request, 'centre/current_bid.html', context)

@login_required(login_url="login")
def viewbid(request, bid_pk):
    bid = get_object_or_404(Bid, pk=bid_pk)
    if request.method == 'GET':
        form = BidForm(instance=bid)
        return render(request, 'centre/viewbid.html', {'bid': bid, 'form': form})
    else:
        try:
            form = BidForm(request.POST, instance=bid)
            form.save()
            return redirect('current_bid')
        except ValueError:
            return render(request, 'centre/viewbid.html', {
                'bid': bid,
                'form': form,
            'error': 'Неверные данные'
            })

@login_required(login_url="login")
def completebid(request, bid_pk):
    bid = get_object_or_404(Bid, pk=bid_pk, user=request.user)
    if request.method == 'POST':
        bid.date_completed = timezone.now()
        bid.save()
        return redirect('current_bid')

@login_required(login_url="login")
def deletebid(request, bid_pk):
    bid = get_object_or_404(Bid, pk=bid_pk, user=request.user)
    if request.method == 'POST':
        bid.delete()
        return redirect('current_bid')

@login_required(login_url="login")
def completedbid(request):
    bids = Bid.objects.filter(user=request.user,
                              date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'centre/completedbid.html', {'bids': bids})
