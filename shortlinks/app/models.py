from django.db import models



class CreatedLinks(models.Model):
    
    url = models.URLField(
        verbose_name='URL'
    )
    
    key = models.CharField(
        verbose_name='key',
        max_length=6,
        unique=True
    )
    
    def __str__(self):
        return self.url
    
    class Meta:
        verbose_name='Created Link'
        verbose_name_plural='Created Links'
