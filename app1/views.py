from django.shortcuts import render


def static_view(request, pk):
    template_name = 'app1/index.html'
    student_list = [1, 2, 3, 4]
    context = {"list": student_list}
    return render(request, template_name, context)
