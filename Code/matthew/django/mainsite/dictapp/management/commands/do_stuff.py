from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'this does stuff'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('hello!')

        # load the file


