from django.shortcuts import render
from django.http import HttpResponse
from .models import (Skill, Education, Experience,
                     Language, SocialLink, PersonalInfo, Fact, Testimonial, Courses)
from .forms import MessageForm
# Create your views here.


def home(request):
    social_links = SocialLink.objects.all()
    personal_info = PersonalInfo.objects.get(user__username = "admin")
    data_home = {
        "social_links": social_links,
        "personal_info": personal_info,
    }

    return render(request, 'home.html', data_home)


def about(request):
    skills = Skill.objects.filter(user__username = "admin")
    personal_info = PersonalInfo.objects.get(user__username = "admin")
    facts = Fact.objects.filter(user__username = "admin")
    testimonials = Testimonial.objects.filter(user__username = "admin")
    data = {
        "skills": skills,
        "personal_info": personal_info,
        "facts": facts,
        "testimonials": testimonials
    }
    return render(request, 'about.html', data)


def resume(request):
    education = Education.objects.filter(user__username = "admin")
    experience = Experience.objects.filter(user__username = "admin")
    language = Language.objects.filter(user__username = "admin")
    courses = Courses.objects.filter(user__username = "admin")
    personal_info = PersonalInfo.objects.get(user__username = "admin")
    data1 = {
        "courses": courses,
        "education": education,
        "experience": experience,
        "language": language,
        "personal_info": personal_info,
    }
    return render(request, 'resume.html', data1)


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("TELL them that sent data is not valid")
    personal_info = PersonalInfo.objects.get(user__username = "admin")
    messageForm = MessageForm()
    
    data_contact ={
    "personal_info": personal_info,
    "messageForm": messageForm
    }
    return render(request, 'contact.html', data_contact )
