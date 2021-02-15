from django.db import models

# Create your models here.
# task name
# date
# status

# create table tasks(task_name varchar,date varchar,status varchar)

class Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=60)

    def __str__(self):
        return self.task_name


# ORM queries
# for creating an object
#     ob=Tasks(task_name="billpayment",date="16/2/2021",status="not completed")
#     ob.save()
# for selecting all objects
#     task=Tasks.objects.all()
# for selecting one particular object
#     task=Tasks.objects.get(id=1)
