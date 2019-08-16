from django.db import models

class Launch(models.Model):
    flight_number = models.TextField()
    launch_date = models.DateTimeField()
    rocket_name = models.TextField()
    mission_patch_link = models.TextField()
    class Meta:
        unique_together = (
            'flight_number',
            'launch_date',
            'rocket_name',
            'mission_patch_link',
        )
