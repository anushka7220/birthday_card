from django.core.management.base import BaseCommand
from card.views import send_birthday_cards

class Command(BaseCommand):
    help = 'Sends scheduled birthday cards'
    
    def handle(self, *args, **options):
        send_birthday_cards()
        self.stdout.write(self.style.SUCCESS('Successfully sent birthday cards'))