from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import BirthdayCard
from .forms import BirthdayCardForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
import datetime
from django.http import JsonResponse

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BirthdayCard
from django.http import JsonResponse

@login_required
def create_card(request):
    if request.method == 'POST':
        # Get data from AJAX request
        color = request.POST.get('color')
        emoji = request.POST.get('emoji')
        date = request.POST.get('date')
        message = request.POST.get('message')
        
        # Create and save card
        card = BirthdayCard(
            user=request.user,
            color=color,
            emoji=emoji,
            date=date,
            message=message
        )
        card.save()
        
        return JsonResponse({'status': 'success', 'card_id': card.id})
    
    return render(request, 'card/create_card.html')

@login_required
def preview_card(request, card_id):
    card = BirthdayCard.objects.get(id=card_id)
    return render(request, 'card/card.html', {'card': card})

def send_birthday_cards():
    today = datetime.date.today()
    unsent_cards = BirthdayCard.objects.filter(
        scheduled_date=today,
        is_sent=False
    )
    
    for card in unsent_cards:
        # Render the card template to a string
        html_content = render_to_string('card/card.html', {'card': card})
        
        # Create email
        email = EmailMessage(
            f"Happy Birthday, {card.recipient.username}!",
            html_content,
            settings.EMAIL_HOST_USER,
            [card.recipient.email],
        )
        email.content_subtype = "html"  # Main content is HTML
        
        try:
            email.send()
            card.is_sent = True
            card.save()
        except Exception as e:
            print(f"Failed to send email to {card.recipient.email}: {e}")


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def cupcake_preview(request):
    return render(request, 'card/cupcake_preview.html')