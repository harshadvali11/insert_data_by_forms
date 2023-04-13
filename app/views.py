from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic insertion is done Successfully')

    return render(request,'insert_topic.html')