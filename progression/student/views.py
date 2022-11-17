from django.shortcuts import render
from .forms import StudentDataForm
from .models import User, Subject, subTopic, subTopicData
from django.http import HttpResponseRedirect
# Create your views here.

from .analysis import average


def index(request):
    students = User.objects.all()
    context = {
        "students": students,

    }
    if request.method == "POST":
        student = request.POST.get('students')
        physicsid = Subject.objects.filter(name__exact="Physics")
        print(physicsid[0].subject_id)
        physicsid = physicsid[0].subject_id
        mathsid = Subject.objects.filter(name__exact="Maths")
        mathsid = mathsid[0].subject_id
        physics_a = average(student, physicsid)
        print(physics_a)
        maths_a = average(student, mathsid)
        studentname = User.objects.filter(student_id__exact=student)
        first_name = studentname[0].firstname
        context = {"avofphysics": physics_a,
                   "avofmaths": maths_a,
                   "first_name": first_name,
                   }

        return render(request, "graph.html", context)
    return render(
        request, "index.html",
        context
    )


def get_topic(request):

    if request.method == 'POST':
        form = StudentDataForm(request.POST)
        if form.is_valid():
            form.save()
            topic = form.cleaned_data.get('topic')
            topic = topic.topic_id
            print(topic)
            request.session['topic'] = topic
            return HttpResponseRedirect('subtopic')
    else:
        form = StudentDataForm()

    students = User.objects.all()

    context = {
        'form': form, 'students': students}

    return render(request, 'topic.html', context)


def get_subtopic(request):
    ratings = [(10, "10"),
               (9, "9"),
               (8, "8"),
               (7, "7"),
               (6, "6"),
               (5, "5"),
               (4, "4"),
               (3, "3"),
               (2, "2"),
               (1, "1"),
               (0, "0"),
               ]
    topic = subTopic.objects.filter(topic__exact=request.session['topic'])
    context = {'topic': topic, 'ratings': ratings}

    return render(request, "subtopicform.html", context)
