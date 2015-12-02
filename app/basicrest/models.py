from django.db import models
from django.utils.translation import gettext as _


class Pet(models.Model):
 
    RACES = (
        ('DOG', _(u'Dog')),
        ('CAT', _(u'Cat')),
        ('COCKATIEL', _(u'Cockatiel'))
    )

    name = models.CharField(max_length=36, default='', db_index=True)
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    race = models.CharField(max_length=6, choices=RACES, null=False, default='DOG', db_index=True)

class PetActivity(models.Model):
    
    ACTIVITIES = (
        ('FEED', _(u'Feed')),
        ('WALK', _(u'Walk')),
        ('PLAY', _(u'Play'))
    )
    
    pet = models.ForeignKey(Pet, null=False, related_name='activities', verbose_name=u"Activities", db_index=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    activity = models.CharField(max_length=4, choices=ACTIVITIES, null=True, db_index=True)