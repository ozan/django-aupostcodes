from django.contrib.localflavor.au.au_states import STATE_CHOICES
from django.db import models


class AUPostCode(models.Model):
    """
    A valid Australian Post Code
    """
    postcode = models.CharField(db_index=True, max_length=4)
    
    class Meta:
        verbose_name = 'Australian Post Code'
        
    def __unicode__(self):
        return self.postcode
    
    @property
    def states(self):
        return tuple(set(pa.state for pa in self.postal_areas.all()))
    

class AUPostalArea(models.Model):
    """
    An Australian postal area
    """
    postcode    = models.ForeignKey(AUPostCode, related_name='postal_areas')
    locality    = models.CharField(max_length=255)
    state       = models.CharField(max_length=3, choices=STATE_CHOICES)
    
    class Meta:
        verbose_name = 'Australian postal area'
        
    def __unicode__(self):
        return "%s (%s)" % (self.locality, self.postcode)

