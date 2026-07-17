from django.db import models
from account.models import CustomUser
from django.utils import timezone
# Create your models here.
class main(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_main')
    team_ma = models.IntegerField(default=0)
    team_ona = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True,blank=True)
    status = models.BooleanField(default=False)
    joker = models.BooleanField()
    
    @property
    def duration(self):
        end = self.finished if self.finished else timezone.now()
        return str(end - self.created).split('.')[0]

    def __str__(self):
        return self.user.phone_number

class game(models.Model):
    main = models.ForeignKey(main,on_delete=models.CASCADE,related_name='game_main')
    buyer = models.IntegerField()
    emtiaz_dast = models.IntegerField()
    color = models.IntegerField()
    emtiaz_ma = models.IntegerField()
    emtiaz_ona = models.IntegerField()
    team_ma = models.IntegerField()
    team_ona = models.IntegerField()
    yasa = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    sh = models.BooleanField(default=False)


