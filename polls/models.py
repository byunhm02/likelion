from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    title=models.CharField(max_length=256)
    description=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    agree=models.IntegerField(default=0)
    disagree=models.IntegerField(default=0)
    
    def agreerate(self):
        total_votes=self.agree+self.disagree
        if total_votes>0:
            return (self.agree/total_votes)*100
        else: 
            return 0
    def disagreerate(self):
        total_votes=self.agree+self.disagree
        if total_votes>0:
            return (self.disagree/total_votes)*100
        else:
            return 0
    
class Poll_agree(models.Model):
    poll_id=models.ForeignKey(Poll,on_delete=models.CASCADE,db_column="poll_id")

class Poll_disagree(models.Model):
    poll_id=models.ForeignKey(Poll,on_delete=models.CASCADE,db_column="poll_id")