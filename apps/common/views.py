import csv
import pytz
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.apps import apps

from apps.ffzusers import models
from .utils import get_export_data
from .constants import table_model_mapping

tz = pytz.timezone("Asia/Calcutta")

@login_required(login_url="/login/")
def export_data(request):
    table_name = None
    field_name = None
    start_date = None
    end_date = None
    if request.GET:
        # print('request.GET',request.GET)
        table_name=request.GET.get('table_name')
        field_name=request.GET.get('field_name')
        start_date=request.GET.get('start_date')
        end_date=request.GET.get('end_date')

    model_choices =[k for k,v in table_model_mapping.items()]
    data = {}
    if not table_name:
        data = {
            'flag': 0,
            'model_choices': model_choices
        }
        context = {'data':data}
        return render(request, 'report/export.html', context)
    
    if table_name and not field_name:
        table_data = table_model_mapping.get(table_name)
        app = table_data.get('app')
        model = table_data.get('model')
        date_range_filter = table_data.get('filters').get('date_filter')
        filters = table_data.get('filters').get('filter_list')

        if filters:
            model_obj = apps.get_model(app, model)
            my_model_fields = filters
            if my_model_fields[0] != 'None':
                my_model_fields.insert(0,'None')
            print(my_model_fields)
            field_choices = my_model_fields
            data = {
                'flag': 1,
                'field_choices': field_choices,
                'table_name': table_name,
                'date_range_filter': date_range_filter

            }
            context = {'data':data}
            return render(request, 'report/export.html', context)
        


    # print('table_name',table_name)
    # print('field_name',field_name)

    if table_name:
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        
        table_data = table_model_mapping.get(table_name)
        app = table_data.get('app')
        model = table_data.get('model')
        model_obj = apps.get_model(app, model)

        total_data = model_obj.objects.all()
        if field_name and field_name != 'None':

            if start_date and end_date:
                field_name_start = '{}__gte'.format(field_name)
                field_name_end = '{}__lte'.format(field_name)

                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                start_date = start_date.replace(tzinfo=tz)

                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                end_date = end_date.replace(tzinfo=tz)

                total_data = total_data.filter(**{field_name_start:start_date},**{field_name_end:end_date})

        my_model_fields = [field.name for field in model_obj._meta.get_fields()]

        writer.writerow(my_model_fields)
        
        for row in total_data.values_list():
            writer.writerow(row)

        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(table_name)

        return response