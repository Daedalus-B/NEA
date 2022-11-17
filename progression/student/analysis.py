from .models import StudentData, Topic


def average(student, subject):
    select_subject = StudentData.objects.filter(
        student__exact=student).filter(subject__exact=subject)

    scores = []
    for i in select_subject:
        scores.append(i.exam_grade)

    n = len(scores)

    if n == 0:
        return "No Data"
    else:
        sumall = 0
        for i in range(0, n):
            sumall = scores[i] + sumall

        current_average = sumall/n

    return current_average
