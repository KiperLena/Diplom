from django.shortcuts import render
from .models import Area


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
