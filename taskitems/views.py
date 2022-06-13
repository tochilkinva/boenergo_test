from django.shortcuts import get_object_or_404, redirect, render

from .forms import ItemForm
from .models import Item
from .task2 import ItemBox


class Results():
    YES = 'YES'
    NO = 'NO'
    UNDEFINED = 'UNDEFINED'


def taskitems(request):
    items = Item.objects.all()
    makeitems = Results.NO
    if items.count() == 0:
        items = None
        makeitems = Results.YES
    else:
        if items.filter(status=True).count() in [10, 100]:
            makeitems = Results.YES

    # пост
    if request.method == 'POST':
        form = ItemForm(request.POST or None)
        if form.is_valid():
            number = form.cleaned_data['number']
            color = form.cleaned_data['color']
            if Item.objects.filter(number=number).exists() is False:
                return redirect('taskitems')
            item = get_object_or_404(Item, number=number)
            # если еще не угадал цвет
            if item.status is False:
                result = Results.NO
                if item.color == color:
                    # цвет угадали
                    item.status = True
                    item.save()
                    result = Results.YES
                context = {
                    'form': form,
                    'Result': result,
                    'Makeitems': makeitems,
                    'Items': items,
                }
                return render(request, 'taskitems.html', context)

            # если уже угадал цвет
            context = {
                'form': form,
                'Result': Results.YES,
                'Makeitems': makeitems,
                'Items': items,
            }
            return render(request, 'taskitems.html', context)

        # если ошибки в форме
        context = {
            'form': form,
            'Result': Results.UNDEFINED,
            'Makeitems': makeitems,
            'Items': items,
        }
        return render(request, 'taskitems.html', context)

    # гет показать пустую форму
    form = ItemForm()
    context = {
        'form': form,
        'Result': Results.UNDEFINED,
        'Makeitems': makeitems,
        'Items': items,
    }
    return render(request, 'taskitems.html', context)


def additems(request, count):
    items = Item.objects.all()
    # есть предметы
    if items.count() != 0:
        for item in items:
            item.delete()
    # нет предметов
    # создаем предметы
    itembox = ItemBox()
    for index in range(count):
        color = itembox.box[index]
        if color == ItemBox.Color.RED:
            color = Item.Colors.RED
        elif color == ItemBox.Color.GREEN:
            color = Item.Colors.GREEN
        else:
            color = Item.Colors.BLUE
        number = index + 1
        item = Item.objects.create(number=number, color=color)
        item.save()

    return redirect('taskitems')
