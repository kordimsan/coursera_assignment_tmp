from django.shortcuts import render


# Create your views here.

def echo(request):
    statement = request.META.get('HTTP_X_PRINT_STATEMENT','empty')
    cont = {}
    if request.method == 'GET':
        cont['params'] = [(k,v) for k,v in request.GET.items()]
        cont['method'] = 'get'
    if request.method == 'POST':
        cont['params'] = [(k,v) for k,v in request.POST.items()]
        cont['method'] = 'post'
    cont['statement'] = statement
    return render(request, 'echo.html', context=cont)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
