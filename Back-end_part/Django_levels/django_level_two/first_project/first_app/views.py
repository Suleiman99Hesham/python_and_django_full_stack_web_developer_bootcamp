from django.shortcuts import render
from first_app.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request):
    Access_list = AccessRecord.objects.order_by('date')
    data_dict = {
        'Access_records' : Access_list,
    }
    return render(request, 'first_app/index.html', context = data_dict)