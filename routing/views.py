from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def simple_route(request):
    if request.method in ['POST', 'PUT']:
        return HttpResponse(status=405)
    return HttpResponse("")

def slug_route(request, param):
    return HttpResponse(param)

def sum_route(request, s1, s2):
    return HttpResponse(int(s1)+int(s2))

@require_http_methods(["GET"])
def sum_get_method(request):
    s1 = request.GET.get('a')
    s2 = request.GET.get('b')
    try:
        return HttpResponse(int(s1)+int(s2))
    except:
        return HttpResponse(status=400)

@require_http_methods(["POST"])
def sum_post_method(request):
    s1 = request.POST.get('a')
    s2 = request.POST.get('b')
    try:
        return HttpResponse(int(s1)+int(s2))
    except:
        return HttpResponse(status=400)
