from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.utils import timezone
from django.contrib import messages

def index(request):

    items = Todo.objects.all()
    return render(request, 'index.html', {'items': items})

def create(request):

    return render(request, 'create.html', {'form_type': 'create'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def save(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    form_type = request.POST.get('form_type')
    id = request.POST.get('id')

    print('Form type received:', form_type)
    print('Form todo id received:', id)


    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))

    if form_type == 'create':
        todo = Todo.objects.create(
        title=title,
        description=description,
        created_at=timezone.now()
        )

        print('New Todo created: ', todo.__dict__)

    elif form_type == 'edit' and id.isdigit():
        todo = Todo.objects.get(pk = id)

        print('Got todo item: ', todo.__dict__)

        todo.title = title
        todo.description = description
        todo.save()

        print('Todo updated: ', todo.__dict__)

    messages.info(request,'Todo item saved.')


    return redirect('index')


def edit(request, id):

    print('received id = ' +str(id))

    todo = Todo.objects.get(pk = id)

    print('Got todo item: ', todo.__dict__)

    return render(request, 'create.html', {'form_type': 'edit','todo':todo})

