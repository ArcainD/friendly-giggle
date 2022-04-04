import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('work_with_database/phones.csv', 'r', encoding='utf-8') as f:
            phones = list(csv.DictReader(f, delimiter=';'))

        for phone in phones:
            release_date = datetime.strptime(
                f"{phone['release_date']}", "%Y-%m-%d"
            )
            Phone.objects.create(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=f'{release_date.date()}',
                lte_exists=phone['lte_exists']
            )
