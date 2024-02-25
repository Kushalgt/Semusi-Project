from django.shortcuts import render
from django.http import HttpResponse  # Fix the import statement

# Create your views here.
def home(request):
   labels = ['32', '34', '36', '38', '40','42','44','46']
   values = [30,31, 32, 33, 36, 37, 40,44]
   return render(request,'index.html', {'labels': labels, 'values': values})
