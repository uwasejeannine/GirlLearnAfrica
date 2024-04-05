from django.shortcuts import render, redirect
from .models import Student, Mentor, Feedback, Course, CommunityEvent
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def home(request):
    students_count = Student.objects.count()
    mentors_count = Mentor.objects.count()
    courses_count = Course.objects.count()
    events_count = CommunityEvent.objects.count()
    return render(request, 'home.html', {'students_count': students_count, 'mentors_count': mentors_count, 'courses_count': courses_count, 'events_count': events_count})

@login_required
def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor_list.html', {'mentors': mentors})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def event_list(request):
    events = CommunityEvent.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def feedback(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Feedback.objects.create(user=request.user, content=content)
        return redirect('home')
    return render(request, 'feedback.html')

@login_required
def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        mentor_id = request.POST.get('mentor')
        mentor = Mentor.objects.get(id=mentor_id)
        Course.objects.create(name=name, description=description, duration=duration, mentor=mentor)
        return redirect('course_list')
    mentors = Mentor.objects.all()
    return render(request, 'add_course.html', {'mentors': mentors})

@login_required
def register_student(request):
    if request.method == "POST":
        # Extract data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        level_of_studies = request.POST.get('level_of_studies')
        program_interested_in = request.POST.get('program_interested_in')
        course_ids = request.POST.getlist('courses')  # Get selected course IDs from multi-select dropdown
        courses = Course.objects.filter(pk__in=course_ids)  # Retrieve Course objects based on IDs
        
        # Create Student object with extracted data
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            level_of_studies=level_of_studies,
            program_interested_in=program_interested_in
        )
        # Add selected courses to the student's courses
        student.courses.set(courses)

        # Redirect to the same page after successful registration
        return redirect('student_list')

    else:
        # Retrieve all available courses
        courses = Course.objects.all()
        # Render the template with available courses
        return render(request, "register_student.html", {"courses": courses})

@login_required
def register_mentor(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        program_interested_in = request.POST.get('program_interested_in')
        
        # Create Mentor object with extracted data
        Mentor.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            program_interested_in=program_interested_in
        )
        
        # Redirect to mentor list after successful registration
        return redirect('mentor_list')
    
    # If it's a GET request, render the registration form
    return render(request, 'register_mentor.html')

@login_required
def course_details(request, course_name):
    course = get_object_or_404(Course, name=course_name)
    return render(request, 'course_details.html', {'course': course})

@login_required
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        CommunityEvent.objects.create(title=title, description=description, date=date, time=time, location=location)
        return redirect('event_list')
    return render(request, 'add_event.html')

@login_required
def view_profile(request):
    user = request.user
    if hasattr(user, 'student'):
        profile = user.student
    elif hasattr(user, 'mentor'):
        profile = user.mentor
    else:
        profile = None
    return render(request, 'profile.html', {'profile': profile})
