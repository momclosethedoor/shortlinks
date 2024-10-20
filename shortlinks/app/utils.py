from string import ascii_uppercase, ascii_lowercase, digits
import random
from .models import CreatedLinks
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def gen_key(length: int)-> str:
    key = ''.join(random.choices(ascii_uppercase + digits + ascii_lowercase, k=length))
    return key

def gen_shortlink(request, url) -> str:
    shortlink = ''
    try:
        link = CreatedLinks.objects.get(url=url)
        shortlink = request.build_absolute_uri(f'/{link.key}')
    except ObjectDoesNotExist:
        key = gen_key(6)
        try:
            link, _ = CreatedLinks.objects.get_or_create(url=url, key=key)
            shortlink = request.build_absolute_uri(f'/{link.key}')
        except IntegrityError:
            gen_shortlink(request, url)
    return shortlink

def get_url_by_key(key):
    try:
        url_obj = CreatedLinks.objects.get(key=key)
    except ObjectDoesNotExist:
        return None
    return url_obj.url

def get_links_list(request):
    GET = request.GET.dict()
    page_num = GET.get('page', 1)
    query = CreatedLinks.objects.all().order_by('-id')
    paginator = Paginator(query, 8)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
