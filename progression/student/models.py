from django.db import models
from django.forms import ModelForm
from django.db import IntegrityError
# Create your models here.


class Subject(models.Model):
    subject_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    name = models.CharField(max_length=50, blank=False)
    mark_for_Astar = models.PositiveSmallIntegerField(blank=False)
    mark_for_A = models.PositiveSmallIntegerField(blank=False)
    mark_for_B = models.PositiveSmallIntegerField(blank=False)
    mark_for_C = models.PositiveSmallIntegerField(blank=False)
    mark_for_D = models.PositiveSmallIntegerField(blank=False)
    mark_for_E = models.PositiveSmallIntegerField(blank=False)
    mark_for_F = models.PositiveSmallIntegerField(blank=False)

    def __str__(self):
        return f'{self.subject_id} - {self.name}'


class User(models.Model):
    student_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    firstname = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=16, blank=False)
    password = models.CharField(max_length=100, blank=False)
    Year = models.IntegerField()
    subject = models.ManyToManyField('Subject')

    def __str__(self):
        return f'{self.student_id} - {self.firstname}'


class Topic(models.Model):
    topic_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class subTopic(models.Model):
    subTopic_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.topic.name} - {self.name}'


class StudentData(models.Model):
    studentData_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    exam_grade = models.IntegerField(blank=False)
    confidence_level = models.IntegerField(blank=False)
    knowledge_level = models.IntegerField(blank=False)
    feedback_from_teacher = models.TextField()

    def __str__(self):
        return f'{self.subject} - {self.student} - {self.topic} - Marks: {self.exam_grade}'


class subTopicData(models.Model):
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
    subTopicData_id = models.BigAutoField(
        primary_key=True, unique=True, default=None)
    studentdata = models.ForeignKey('StudentData', on_delete=models.CASCADE)
    subtopic = models.CharField(max_length=100)
    rating = models.IntegerField(choices=ratings)


class Target_Grade(models.Model):
    grades = [("80%", "A*"),
              ("70%", "A"),
              ("60%", "B"),
              ("50%", "C"),
              ("40%", "D"),
              ("30%", "E"), ]

    student = models.ForeignKey('User', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    personal_grade = models.CharField(
        choices=grades, max_length=4, blank=False)
    target_grade = models.CharField(choices=grades, max_length=4, blank=True)

    def __str__(self):
        return f'{self.subject} - {self.student} - {self.personal_grade}'
