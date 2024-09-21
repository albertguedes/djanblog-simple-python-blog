from django.test import TestCase
from djanblog.models.post import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.post = Post.objects.create(
            title='test',
            description='test',
            content='test'
        )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_content_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('description').max_length
        self.assertEquals(max_length, 512)
