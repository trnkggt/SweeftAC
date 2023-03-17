import string
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


from .models import Url
# Create your views here.

## Call to create a shortened url
# {"longurl":"URL"}
## Call to create a shortened url if user is premium
# {"is_premium":true, "custom":"CUSTOM_NAME", "longurl":"URL"}


@api_view(['POST'])
def urlshortener(request):
    url = request.data.get('longurl')
    is_premium = request.data.get('is_premium')
    shorturl = None
    characters_for_url = (string.ascii_uppercase +
                          string.ascii_lowercase +
                          string.digits
                          )
    if is_premium:
        custom_name = request.data.get('custom')
        obj = Url.objects.filter(shorturl=custom_name).exists()
        if obj:
            return Response({'error':"this name is already taken"})
        else:
            shorturl = custom_name
            Url.objects.create(longurl=url, shorturl=shorturl, is_premium=True)
    else:
        while True:
            short_url = ''.join(random.choice(characters_for_url) for i in range(6))
            try:
                Url.objects.get(shorturl=short_url)
            except ObjectDoesNotExist:
                shorturl=short_url
                break
        Url.objects.create(longurl=url, shorturl=shorturl)

    return Response({'longurl':url, 'shorturl':'127.0.0.1:8000/'+shorturl})

def urlviewer(request, shorturl):
    try:
        obj = Url.objects.get(shorturl=shorturl)
    except ObjectDoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longurl)