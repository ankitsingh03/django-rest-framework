from django.core.management.base import BaseCommand
from data.models import Umpire, Deliveries, Matches
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file1')
        parser.add_argument('csv_file2')
        parser.add_argument('csv_file3')

    def handle(self, *args, **options):
        with open(options["csv_file1"], 'r') as file:
            csv_reader = csv.reader(file)
            csv_reader.__next__()
            data = [Umpire(
                name=line[0],
                nationality=line[1],
                first_officiated=line[2],
                last_officiated=line[3],
                Number_of_Matches=line[4]
                            ) for line in csv_reader]
            Umpire.objects.bulk_create(data)

        with open(options['csv_file2'], 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_reader.__next__()
            data = [Deliveries(
                        match_id=line[0],
                        batting_team=line[2],
                        batsman=line[6],
                        batsman_runs=line[-6],
                        total_runs=line[-4]
                                ) for line in csv_reader]
            Deliveries.objects.bulk_create(data)

        with open(options['csv_file3'], 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_reader.__next__()
            data = [Matches(
                season=line[1],
                team1=line[4],
                team2=line[5]) for line in csv_reader]
        Matches.objects.bulk_create(data)

        self.stdout.write(self.style.SUCCESS('data Push Successfully'))
