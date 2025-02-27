from django.db import models


# Create your models here.
class Topics(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TopicNotes(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    link = models.TextField()


class PastPaper(models.Model):
    year = models.DateField()
    name = models.CharField(max_length=200)
    link = models.TextField()

    paper_choices = [
        ("P1", "Paper 1"),
        ("P2", "Paper 2")
    ]

    type_choices = [
        ("QP", "Question paper"),
        ("MS", "Marking scheme"),
        ("IN", "Insert")
    ]

    type = models.CharField(max_length=2, choices=type_choices)
    paper = models.CharField(max_length=2, choices=paper_choices)
