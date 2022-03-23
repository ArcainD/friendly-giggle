from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    temp_dict = DATA['omlet'].copy()

    for key, value in temp_dict.items():
        temp_dict[key] = temp_dict[key] * servings

    context = {
        'recipe': temp_dict
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    temp_dict = DATA['pasta'].copy()

    for key, value in temp_dict.items():
        temp_dict[key] = temp_dict[key] * servings

    context = {
        'recipe': temp_dict
    }
    return render(request, 'calculator/index.html', context)


def buter_view(request):
    servings = int(request.GET.get('servings', 1))
    temp_dict = DATA['buter'].copy()

    for key, value in temp_dict.items():
        temp_dict[key] = temp_dict[key] * servings

    context = {
        'recipe': temp_dict
    }
    return render(request, 'calculator/index.html', context)
