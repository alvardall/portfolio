from django.shortcuts import render
from django.http import HttpResponse
from .models import (Skill, Education, Experience,
                     Language, SocialLink, PersonalInfo, Fact, Testimonial, Courses)
# Create your views here.


def home(request):
    social_links = SocialLink.objects.all()
    personal_info = PersonalInfo.objects.first()
    data_home = {
        "social_links": social_links,
        "personal_info": personal_info,
    }

    return render(request, 'home.html', data_home)


def about(request):
    skills = Skill.objects.all()
    personal_info = PersonalInfo.objects.first()
    facts = Fact.objects.all()
    testimonials = Testimonial.objects.all()
    data = {
        "skills": skills,
        "personal_info": personal_info,
        "facts": facts,
        "testimonials": testimonials
    }
    return render(request, 'about.html', data)


def resume(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    language = Language.objects.all()
    courses = Courses.objects.all()
    data1 = {
        "courses": courses,
        "education": education,
        "experience": experience,
        "language": language,
    }
    return render(request, 'resume.html', data1)


def services(request):
    return render(request, 'services.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')
