from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class PersonalInfo(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(validators=[EmailValidator])
    city = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=30)
    freelance = models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return f"{self.first_name}"

class Skill(models.Model):
    name = models.TextField(max_length =20)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default = 1)

    def __str__(self) -> str:
        return f'{self.name} skill value is {self.value}'

class Courses(models.Model):
    program = models.TextField(max_length =40)
    program_name = models.TextField(max_length =40)
    cours_name = models.TextField(max_length =40)

    def __str__(self) -> str:
        return f'{self.cours_name}'


class Education(models.Model):
    university_name = models.TextField()
    start_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1990)])
    end_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1990)])
    grade = models.TextField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.university_name}  {self.grade}'


class Experience(models.Model):
    position_name = models.TextField(max_length=30, blank=True, null=True)
    start_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    company_name = models.TextField(max_length=70)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.position_name} in {self. company_name}'
    
class Language(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.level}"
    
class SocialLink(models.Model):
    link = models.URLField()
    link_name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.link_name}"
    
class Fact(models.Model):
    name = models.TextField(max_length=50)
    number = models.PositiveIntegerField(validators=[MaxValueValidator(10000), MinValueValidator(0)])
    
    def __str__(self) -> str:
        return f"{self.name} - {self.number}"
    
class Testimonial(models.Model):
    name = models.CharField(max_length=40)
    job_position = models.CharField(max_length=40)
    opinion = models.CharField(max_length=250)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.name}, {self.job_position}"

