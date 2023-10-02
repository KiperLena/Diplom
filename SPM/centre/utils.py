from .models import Area
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q #для поиска

def search_area(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')  # перезаписываем значение методом get

    license_area = Area.objects.filter(
        Q(title__icontains=search_query) |
        Q(region__icontains=search_query)
    )
    return license_area, search_query

def paginate_area(request, license_area, pr):
    # pr = 24
    paginator = Paginator(license_area, pr)
    page = request.GET.get('page')

    try:
        license_area = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        page = 1
        license_area = paginator.page(page)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        page = paginator.num_pages
        license_area = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, license_area
