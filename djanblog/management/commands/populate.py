from django.core.management.base import BaseCommand
from djanblog.models import Post
from faker import Faker
from datetime import datetime, timedelta
from random import randint

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos'

    def handle(self, *args, **kwargs):
        fake = Faker()
        today = datetime.now()
        for i in range(10):
            random_days = fake.random_int(min=1, max=365)
            created = today - timedelta(days=random_days)
            post = Post(
                title=fake.sentence().rstrip('.').lower(),
                description=fake.sentence(),
                content=fake.text(),
                published=randint(0, 1),
            )            
            post.created_at = created
            post.updated_at = created
            post.save() 
            
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
