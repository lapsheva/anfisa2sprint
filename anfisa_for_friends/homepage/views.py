from django.shortcuts import render
from django.db.models import Q

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        (Q(is_on_main=True) & Q(is_published=True))
        | Q(title__contains='пломбир') & Q(is_published=True)
    )
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
