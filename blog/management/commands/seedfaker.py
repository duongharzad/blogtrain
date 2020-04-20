from datetime import timezone
from random import randrange

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker
from faker.generator import random

from blog.models import Post

fake = Faker(['en_US'])


class Command(BaseCommand):
    help = 'Fake data'

    def add_arguments(self, parser):
        parser.add_argument('record', type=int, help='ABC')

    def handle(self, *args, **options):
        records = options['record']

        list_user = User.objects.all()

        for _ in range(0, records):
            id = random.randint(1, 4)
            title = fake.name()
            status = random.choice(['published', 'draft'])
            Post.objects.create(title=title + " Post!!!",
                                author=random.choice(list_user),
                                slug="-".join(title.lower().split()),
                                body=fake.text(),
                                created=fake.date(),
                                updated=fake.date(),
                                )
