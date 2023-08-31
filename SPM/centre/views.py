from django.shortcuts import render, redirect
from .models import Area, Department1, Group, Department2,Directorate
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
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
    return render(request, 'centre/index.html', context)


def centre(request):
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
    return render(request, 'centre/centre.html', context)


def area(request, pk):

    licenses = Area.objects.get(id=pk)

    return render(request, 'centre/area.html')


def old_doc(request):
    return render(request, 'centre/biblioteka.html')

@login_required(login_url="login")
def create_report(request):
    form = ReportForm()

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'centre/form-report.html', context)

