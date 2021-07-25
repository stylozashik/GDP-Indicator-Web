from django.shortcuts import render
from django.http import HttpResponse
from .models import YearlyGDP
import pandas
import joblib


# Create your views here.
def home(request):

    # Taking parameter
    raw_data = joblib.load('prediction.sav')
    print(raw_data)
    

    context = {
        'y_count' : 2021,
        'data' : joblib.load('prediction.sav'),
        }
    return render(request , 'home.html' ,context)

def search(request):
    if request.method == "POST":
        searched = request.POST['query']
        gdp_growth  = YearlyGDP.objects.filter(year__contains=searched)
        return render(request , 'search.html' , {'searched' : searched , 'gdp_growth':gdp_growth})
    else:
        return render(request , 'search.html')