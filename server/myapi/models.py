from django.db import models

"""
TODO implement validators
- nullable or sure
"""

class Film(models.Model):

    class MovieFormat(models.TextChoices):
        ANALOG_35 = '35mm'
        DVD = 'DVD'
        BLU_RAY = 'Blu ray'

    class LanguageSubtitles(models.TextChoices):
        FRENCH = 'VOF'
        FOREIGN = 'VOSTFR'

    projection_date = models.DateTimeField()
    title = models.CharField(max_length=60)
    actors = models.JSONField(default="[]")
    director = models.CharField(max_length=60)
    duration = models.DurationField()
    synopsis = models.TextField()
    origin_country = models.CharField(max_length=60)
    release_year = models.SmallIntegerField()
    trailer_link = models.URLField()
    is_in_color = models.BooleanField()
    movie_format = models.CharField(max_length=20, choices=MovieFormat.choices)
    language_subtitles = models.CharField(max_length=20, choices=LanguageSubtitles.choices)
    poster_link = models.URLField()
    banner_link = models.URLField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} de {self.director} ({projection_date.strftime("%d/%m/%Y")})'

