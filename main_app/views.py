from django.shortcuts import render

from .models import Finch

from django.views.generic.edit import CreateView, UpdateView, DeleteView


#define home view
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    """ grab all data from model """
    finches = Finch.objects.all()

    return render(request,'finches/index.html',{
    
        'finches': finches
    })

def finches_detail(request, finch_id):
    """ finch id from utl specific show function """
    finch = Finch.objects.get(id=finch_id)
  

    return render(request,'finches/detail.html',{
        'finch': finch
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch

  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'