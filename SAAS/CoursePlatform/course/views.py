from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the uploaded file is a PDF
            if 'document' in request.FILES:
                uploaded_file = request.FILES['document']
                if not uploaded_file.name.endswith('.pdf'):
                    return render(request, 'create_course.html', {'form': form, 'error_message': "Only PDF files are allowed."})
            else:
                return render(request, 'create_course.html', {'form': form, 'error_message': "No file uploaded."})
            
            # Set the instructor_id before saving the form
            form.instance.instructor_id = request.user.id
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

@login_required
def course_list(request):
    courses = Course.objects.all()

    if request.user.is_authenticated:
        for course in courses:
            course.is_unlocked = request.user in course.subscribers.all()
    else:
        for course in courses:
            course.is_unlocked = False
    
    context = {
        "courses": courses
    }

    return render(request, "course_list.html", context)

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user not in course.subscribers.all():
        return redirect("course_list")

    context = {
        "course": course
    }

    return render(request, "course_detail.html", context)

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Check if the user is a superuser
    if request.user.is_superuser:
        course.delete()
        return redirect('course_list')
    else:
        # If the user is not authorized to delete the course, redirect back to the course detail page
        return redirect('course_detail', course_id=course_id)
