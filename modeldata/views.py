from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from modeldata.models import Item
from modeldata.serializers import ItemSerializer
import logging

logger = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def item_list(request):
	print("servicing request...");
	if request.method == 'POST':
		print("servicing POST request...");
		print("request is: ")
		print(request);
		data = JSONParser().parse(request)
		print("data is: ");
		print(data);
		serializer = ItemSerializer(data=data)
		return JSONResponse(serializer.data, status=201)
	elif request.method == 'GET':
	        items = Item.objects.all()
	        serializer = ItemSerializer(items, many=True)
	        return JSONResponse(serializer.data)
