from django.shortcuts import render
from .models import Area




def centre(request):
    license_area = Area.objects.all()
    context = {
        'area': license_area,
    }
    return render(request, 'centre/centre.html', context)


def area(request, pk):
    licenses = Area.objects.get(id=pk)
    return render(request, 'centre/license_area.html', {'license': licenses})
