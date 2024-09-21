from django.test import TestCase
from django.urls import reverse
from djanblog.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Título de teste', content='Conteúdo de teste')
        self.response = self.client.get(reverse('post', args=[self.post.id]))

    def test_post_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_view_template(self):
        self.assertTemplateUsed(self.response, 'post.html')

    def test_post_view_context(self):
        self.assertIsInstance(self.response.context['post'], Post)

    def test_post_view_contains_post_title(self):
        self.assertContains(self.response, self.post.title)

    def test_post_view_contains_post_content(self):
        self.assertContains(self.response, self.post.content)
