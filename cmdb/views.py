from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.shortcuts import HttpResponse


def index(request):
    devs_df = pd.read_excel('cmdb/inventory.xlsx')
    devs = devs_df.to_dict(orient='records')
    data = {'devs':devs}
    return render(request, 'cmdb/index.html', context=data)