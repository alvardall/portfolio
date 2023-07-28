from django.contrib import admin
from .models import (Skill, Education, Experience,
                    Language, SocialLink, PersonalInfo, Fact, Testimonial, Courses, Message, PortfolioProject )


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date",
                    "end_date", "grade", "created_on"]
    list_filter = ["start_date"]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "user"]
    list_filter = ["value"]
    search_fields = ["name"]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "created_on"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["position_name", "start_date",
                    "end_date", "company_name", "created_on"]
    list_filter = ["start_date"]


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["link", "link_name", "created_on"]


class FactAdmin(admin.ModelAdmin):
    list_display = ["name", "number"]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "job_position", "created_on"]


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(PersonalInfo)
admin.site.register(Fact, FactAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Courses)
admin.site.register(Message)
admin.site.register(PortfolioProject)

