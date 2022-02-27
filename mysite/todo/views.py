from django.shortcuts import redirect, render
from todo.forms import SubjectForm, TaskForm
from todo.models import Subject



def home(request):
    subjects = Subject.objects.all
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SubjectForm()

    context = {'subjects':subjects,'form':form}
    return render(request, 'todo/home.html', context)



def deleteSubject(request, pk):
    subject = Subject.objects.get(id=pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('home')

    return render(request, 'todo/delete.html', {'subject':subject})


def updateSubject(request, pk):
    subject = Subject.objects.get(id=pk)

    form = TaskForm(instance=subject)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'todo/update.html', context)