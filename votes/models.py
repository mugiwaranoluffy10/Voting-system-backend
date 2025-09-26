from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes_cast')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes_received')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'candidate')

    def __str__(self):
        return f"{self.voter.username} -> {self.candidate.username}"
