from django.test import TestCase
from api.models import Snippet
from django.contrib.auth.models import User

# Create your tests here

class SnippetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        snippet = Snippet(title="python example", code="print(hello world)",linenos=True, owner=self.user)
        snippet.save()

    def test_user(self):
        self.assertEqual(self.user.username, "testuser")

    def test_snippet(self):
        self.assertEqual(Snippet.objects.filter(title="python example")[0].title, "python example")
        self.assertEqual(Snippet.objects.filter(title="python example")[0].owner, self.user)
