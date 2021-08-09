from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Xmind_file(models.Model):
    username = models.CharField(max_length = 30)
    file = models.FileField(upload_to = 'upload/')

    def __unicode__(self):
        return self.username
