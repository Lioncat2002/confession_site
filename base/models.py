from django.db import models

class Confessions(models.Model):
    title=models.CharField(max_length=200)
    confession=models.TextField(null=False,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
      ordering=['-created']

    def __str__(self):
        return self.title+" created on: "+str(self.created.date())

