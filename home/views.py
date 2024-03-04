from django.shortcuts import render
from django.http import HttpResponse  # Fix the import statement

# Create your views here.
def home(request):
   labels = ['32', '34', '36', '38', '40','42','44','46']
   values = [32,32, 33, 33, 33.5, 34, 33,35]
   average=0
   for value in values:
      average+=value
   average/=len(values)
   return render(request,'index.html', {'labels': labels, 'values': values,'averages' : average})
