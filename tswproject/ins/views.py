from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from ins.models import Subject, Instruction, Task, Snippet
# Create your views here.
def home(request):
    c = RequestContext(request)
    subject_list = Subject.objects.all()[:5]
    return render_to_response('ins/index.html', {'subject_list': subject_list}, c)

def subject(request, subject_id):
    c = RequestContext(request)
    s = Subject.objects.get(id = subject_id)
    instructions_list = s.instruction_set.all()[0:5]
    return render_to_response('ins/subject.html', {'instructions_list': instructions_list})

def instruction(request, instruction_id):
    c = RequestContext(request)
    instruction = Instruction.objects.get(id = instruction_id)
    task_list = instruction.task_set.all()[0:5]
    task_list = [ [task, task.snippet_set.all()] for task in task_list]
    return render_to_response('ins/instruction.html', {'instruction': instruction, 'task_list': task_list})

def loginuser(request):
    c = RequestContext(request)
    password = request.POST['password']
    username = request.POST['username']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Sucessfull log-in!')
        return redirect('/')
    messages.add_message(request, messages.WARNING, 'Unsucessfull log-in!')
    return redirect('/')
    
     

def logoutuser(request):
    c = RequestContext(request)
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Sucessfull log-out!')
    return redirect('/')
