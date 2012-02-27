from django.shortcuts import render_to_response
from ins.models import Subject, Instruction, Task, Snippet
# Create your views here.
def home(request):
    subject_list = Subject.objects.all()[:5]
    return render_to_response('ins/index.html', {'subject_list': subject_list})

def subject(request, subject_id):
    s = Subject.objects.get(id = subject_id)
    instructions_list = s.instruction_set.all()[0:5]
    return render_to_response('ins/subject.html', {'instructions_list': instructions_list})

def instruction(request, instruction_id):
    instruction = Instruction.objects.get(id = instruction_id)
    task_list = instruction.task_set.all()[0:5]
    task_list = [ [task, task.snippet_set.all()] for task in task_list]
    return render_to_response('ins/instruction.html', {'instruction': instruction, 'task_list': task_list})
