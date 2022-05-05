from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import ffz_vegitables,ffz_category
import pandas as pd
from pandas import DataFrame
# Create your views here.

def vegitableView(request):
    if request.method=='GET':
        categories=ffz_category.objects.values('name')
        vegitables=ffz_vegitables.objects.filter(veg_type__name='vegetables')
        return render(
            request,
            'temp/vegitable.html',
            {
                'vegitables':vegitables,
                'categories':categories,
                }
            )
    if request.method=='POST':
        categories=ffz_category.objects.values('name')
        excel_file=request.FILES['myfile']
        df=pd.read_excel(excel_file).fillna(0)
        data=df.to_dict('records')
    return render(request,
                  'temp/vegitable.html',
                  {
                      'vegitables':list(data),
                      'categories':categories,
                      }
                  )
        
def getVegitable(request):
    if request.method=='POST':
        category=request.POST.get('category')
        print('ok')
        vegitables=ffz_vegitables.objects.filter(veg_type__name=category).values()
        print(vegitables)
        return JsonResponse({'filtered_vegData':list(vegitables)})            