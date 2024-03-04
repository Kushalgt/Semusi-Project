from django.shortcuts import render
from django.http import HttpResponse  # Fix the import statement

# Create your views here.
def home(request):
   labels = ['32', '34', '36', '38', '40','42','44','46']
   values = [32,32, 33, 33, 33.5, 34, 33,35]
   return render(request,'index.html', {'labels': labels, 'values': values})
