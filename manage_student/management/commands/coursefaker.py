from manage_student.models import CourseModel
from faker import Faker
from django.core.management.base import BaseCommand
import random
from datetime import date, datetime

faker = Faker(['en-US', ])


class Command(BaseCommand):
    help = 'Faker data'

    def add_arguments(self, parser):
        parser.add_argument('records', type=int, help='Create records')

    def handle(self, *args, **options):
        records = options['records']
        list_course = ['D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19']

        for i in range(0, records):
            CourseModel.objects.create(
                name_course=list_course[i],
                start_date=faker.date(),
                end_date=faker.date(),
            )
