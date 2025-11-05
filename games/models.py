from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    min_players = models.IntegerField()
    max_players = models.IntegerField()

    year_published = models.IntegerField(blank=True, null=True)

    image_url = models.URLField(blank=True, null=True)

    bgg_id = models.CharField(max_length=50, blank=True, null=True, help_text="BoardGameGeek Game ID")

    def __str__(self):
        return self.title
