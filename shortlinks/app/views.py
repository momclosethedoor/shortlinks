from django.shortcuts import redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotFound
from django.template.response import TemplateResponse

from .utils import *

def index(request):
    return redirect('/shortlinks/create')

def get_url(request, key_url):
    url = get_url_by_key(key_url)
    if url is None:
        return HttpResponseNotFound('INVALID LINK')
    return redirect(url)

def links_list(request):
    context = {}
    context['page_obj'] = get_links_list(request)
    context['domain'] =  request.build_absolute_uri('/')
    return TemplateResponse(request, 'links.html', context=context)

class ShortLinksView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        url = request.POST['url']
        x = gen_shortlink(request, url)
        response = {'shortlink': x}
        return JsonResponse(data=response)

