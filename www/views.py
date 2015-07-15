from django.shortcuts import render, redirect
from django.core import serializers
from django.conf import settings
import json
from django.http import HttpResponse, JsonResponse
from repositories.device_repository import DeviceRepository
from repositories.user_repository import UserRepository
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
@require_GET
def index(request):
    dr = DeviceRepository()
    devices = dr.get_all_devices()
    free_devices = list(filter((lambda x: x.reserved_by is None), devices))

    return render(request, 'www/index.html', {
        'devices': devices,
        'free_devices': free_devices
    })

@require_GET
def login(request):
    return render(request, 'www/login.html', {})

@login_required(login_url=settings.LOGIN_URL)
@require_GET
def reserve(request):
    device_pk = request.GET.get('device_pk', '')
    user_pk = request.GET.get('user_pk', '')

    dr = DeviceRepository()
    ur = UserRepository()

    device = dr.get_by_pk(device_pk)
    user = ur.get_by_pk(user_pk)

    device.reserve(user)

    return redirect('devices:index')

@login_required(login_url=settings.LOGIN_URL)
@require_GET
def free(request, pk):
    dr = DeviceRepository()
    device = dr.get_by_pk(pk)
    device.set_free()

    return redirect('devices:index')

@login_required(login_url=settings.LOGIN_URL)
@require_GET
def users(request):
    last_name = request.GET.get('last_name', '')
    ur = UserRepository()

    users = ur.get_by_last_name(last_name)

    json_users = json.loads(serializers.serialize('json', users))

    response = {'suggestions': []}

    for user in json_users:
        response['suggestions'].append({
            'value': ' '.join([user['fields']['first_name'], user['fields']['last_name']]),
            'data': user['pk']
        })

    return JsonResponse(response, safe=False)
