from django.core.management.base import NoArgsCommand
# from culturals.models import Cultural as event


class Command(NoArgsCommand):
    help = 'Expires event objects which are out-of-date'
