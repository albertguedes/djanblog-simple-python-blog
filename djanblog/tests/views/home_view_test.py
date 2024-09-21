from django.test import TestCase
from djanblog.models.post import Post
from django.db.models import QuerySet 

class HomeViewTest(TestCase):
    def setUp(self):
        for i in range(10):
            Post.objects.create(title=f'Título {i}', content='Conteúdo de teste')
        self.response = self.client.get('/')

    def test_home_view_pagination(self):
        self.assertEqual(len(self.response.context['posts']), 10)

    def test_home_view_posts(self):
        posts = self.response.context['posts']
        self.assertIsInstance(posts, QuerySet)
        self.assertTrue(posts.exists())
