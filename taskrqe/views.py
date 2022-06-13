from django.shortcuts import get_object_or_404, render

from .forms import RQEForm
from .models import RQE
from .task1 import roots_quadratic_equation


def taskrqe(request):
    # пост
    if request.method == 'POST':
        form = RQEForm(request.POST or None)
        if form.is_valid():
            coefa = form.cleaned_data['coefa']
            coefb = form.cleaned_data['coefb']
            coefc = form.cleaned_data['coefc']
            # уже есть решение в базе, показать
            rqe_status = RQE.objects.filter(
                coefa=coefa, coefb=coefb, coefc=coefc).exists()
            if rqe_status:
                rqe_result = get_object_or_404(
                    RQE, coefa=coefa, coefb=coefb, coefc=coefc)
                noroots = False
                if rqe_result.root1 is None and rqe_result.root2 is None:
                    noroots = True
                context = {
                    'form': form,
                    'Root1': rqe_result.root1,
                    'Root2': rqe_result.root2,
                    'Result': True,
                    'Noroots': noroots,
                }
                return render(request, 'taskrqe.html', context)
            # еще нет решения в базе, посчитать, показать
            rqe_result = form.save(commit=False)
            roots = roots_quadratic_equation(coefa, coefb, coefc)
            rqe_result.root1 = roots[0]
            rqe_result.root2 = roots[1]
            rqe_result.save()
            noroots = False
            if rqe_result.root1 is None and rqe_result.root2 is None:
                noroots = True
            context = {
                    'form': form,
                    'Root1': rqe_result.root1,
                    'Root2': rqe_result.root2,
                    'Result': True,
                    'Noroots': noroots,
            }
            return render(request, 'taskrqe.html', context)

        # если ошибки в форме
        context = {
            'form': form,
            'Result': False,
        }
        return render(request, 'taskrqe.html', context)

    # гет. показать пустую форму
    form = RQEForm()
    context = {
        'form': form,
        'Result': False,
    }
    return render(request, 'taskrqe.html', context)
