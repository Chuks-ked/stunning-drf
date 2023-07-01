import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # print(dir(request))
    # request.body
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    return JsonResponse(data)