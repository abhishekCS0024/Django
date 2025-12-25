from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def todo_list(req):
    return render(req, 'todo1\index.html')

def create_todo(req):
    if req.method == 'POST':
        title = req.POST.get('title')   
        description = req.POST.get('description')   
        todo = Todo.objects.create(title=title, description=description)
    return redirect('todo_list')
        
