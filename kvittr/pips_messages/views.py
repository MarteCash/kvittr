from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from pips_messages.models import Pip


def pip_listing(request):
    if request.method == 'POST':
        new_pip = request.POST.get('new_pip')
        if new_pip:
            pip = Pip()
            pip.pip = new_pip
            pip.created_datetime = timezone.now()
            pip.created_by = request.user
            pip.save()

    pips = Pip.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(pips, 5)
    try:
        pips = paginator.page(page)
    except PageNotAnInteger:
        pips = paginator.page(1)
    except EmptyPage:
        pips = paginator.page(paginator.num_pages)

    context = {
        'pips': pips,
        }
    return render(request, 'pips_messages/pip_listing.html', context)


def pip_details(request, post_id):
    pip = Pip.objects.get(pk=post_id)
    context = {'pip': pip}
    return render(request, 'pips_messages/pip_details.html', context)    


@login_required
def pip_add_likes(request, pip_id):
    pip = Pip.objects.get(pk=pip_id)
    pip.likes = pip.likes + 1
    pip.save()
    data = {'likes_updated': pip.likes}
    return JsonResponse(data)
