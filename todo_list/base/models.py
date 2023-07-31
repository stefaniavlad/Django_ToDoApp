from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # create one-to-many relationship -> one user can have many items
    # on_delete what do we do with a task if the user gets deleted -> we will delete the task as well
    # null=True in theory in the database this field could be empty=Null
    # whenever we submit a form we want to allow that value to be blank
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # CharField is usually used for Headline, Name or simple values
    # TextField is used to create a box to write a message
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # default=False -> because when an item is first created we do not want ti to be True/Completed already
    complete = models.BooleanField(default=False)
    # auto_now_add it takes a snapshot of the time when the task was created and put it in date time
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # set the default value to title
        return self.title

    class Meta:
        # set the default ordering by task complete
        # every complete status should be sent to the bottom of the list because they are done
        ordering = ['complete']