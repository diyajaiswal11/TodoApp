from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from .models import Task
from .forms import TaskForm

class TaskList(View):
    def get(self,request):
        form=TaskForm() 
        tasks=Task.objects.all()
        return render(request,'tasklist.html',{'form':form,'tasks':tasks})


    def post(self,request):
        form=TaskForm(request.POST) 
        if form.is_valid():
            new_task=form.save() 
            return redirect('task_list_url') 
        else:
            return redirect('task_list_url') 

