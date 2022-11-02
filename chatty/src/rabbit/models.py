from django.db import models
# from django.contrib.auth.models import User
from blog.models import CustomUser
import hashlib


class Ribbit(models.Model):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()


CustomUser.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])