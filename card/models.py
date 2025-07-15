from django.db import models
from django.contrib.auth.models import User

class BirthdayCard(models.Model):
    THEME_CHOICES = [
        ('balloons', 'Balloons'),
        ('cake', 'Cake'),
        ('gifts', 'Gifts'),
        ('nature', 'Nature'),
    ]
    
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
    ]
    
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_cards')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_cards')
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='balloons')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='red')
    emojis = models.CharField(max_length=100, default='🎂🎈🎉')
    message = models.TextField()
    scheduled_date = models.DateField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Card for {self.recipient.username} on {self.scheduled_date}"