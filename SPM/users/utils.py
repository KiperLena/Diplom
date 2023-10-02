from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Account
from django.db.models import Q #для поиска


def search_profiles(request): #поисковая строка
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')  # перезаписываем значение

    prof = Account.objects.filter(Q(name__icontains=search_query) |
                                  Q(profession__icontains=search_query) |
                                  Q(department__icontains=search_query))
    return prof, search_query


def paginate_profiles(request, license_area, pr): #пагинация
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

    left_index = int(page) - 4 #сколько слева

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5 #сколько справа

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, license_area
