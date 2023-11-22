from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    name=models.TextField()
    user1=models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name='conversations_user1',
                                null=True,
                                default=None
                            )
    user2=models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name='conversations_user2',
                                null=True,
                                default=None
                            )
    def save(self,*args,**kwargs):
        if self.name=='rename':
            self.name=f'{self.user1.username}_{self.user2.username}'
        return super().save(*args,**kwargs)

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    class Meta:
        ordering=['-created']