from django.shortcuts import render, get_object_or_404


from .models import Course, Step


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    context = {
        'course': get_object_or_404(Course, pk=pk)
    }
    return render(request, 'courses/course_detail.html', context)


def step_detail(request, course_pk, step_pk):
    context = {
        'step': get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    }
    return render(request, 'courses/step_detail.html', context)