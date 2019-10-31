import datetime

from django.db import models
from django.utils import timezone

class TodoList( models.Model ):
    item = models.CharField( max_length=300 )
    status = models.IntegerField( default=0 )
    pub_date = models.DateTimeField( 'published date and time' )

    def __str__(self):
        return self.item
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

