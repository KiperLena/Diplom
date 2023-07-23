from django.shortcuts import render
from .models import Area
from .forms import ReportForm


def index(request):
    return render(request, 'centre/index.html')


def centre(request):
    license_area = Area.objects.all()
    context = {
        'area': license_area,
    }
    return render(request, 'centre/centre.html', context)


def area(request, pk):
    licenses = Area.objects.get(id=pk)
    return render(request, 'centre/license_area.html', {'license': licenses})


def old_doc(request):
    return render(request, 'centre/biblioteka.html')


def create_report(request):
    form = ReportForm()
    context = {'form': form}
    return render(request, 'centre/form-report.html', context)

