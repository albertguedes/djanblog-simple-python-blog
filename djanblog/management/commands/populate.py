from django.core.management.base import BaseCommand
from djanblog.models import Post
from faker import Faker
from datetime import datetime, timedelta
from random import randint
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos'

    fake = Faker()        
    
    def handle(self, *args, **kwargs):

        today = datetime.now()
        
        for i in range(1):

            random_days = self.fake.random_int(min=1, max=365)

            author = User.objects.order_by('?').first()                        
            title = self.fake.sentence().rstrip('.').lower()
            description = self.fake.paragraph()
            content = self.generateContent()        
            published = randint(0, 1)
            
            post = Post(
                author=author,
                title=title,
                description=description,
                content=content,
                published=published,
            )            
            
            created = today - timedelta(days=random_days)
            post.created_at = created
            post.updated_at = created
            
            post.save() 
            
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))

    def generateContent(self):
        content = ''        
        for i in range(50):
            content += self.fake.paragraph() + '\n'
            if randint(i, 50) == i:
                content += '<br><br>'
                
        return content