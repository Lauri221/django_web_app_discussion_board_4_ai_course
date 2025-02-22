from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse

from .models import Discussion  # Ensure you have a Discussion model defined

class DiscussionTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test discussion instance.
        # Adjust the fields (e.g., title, content) according to your actual model.
        self.discussion = Discussion.objects.create(title="Test Discussion", content="This is a test discussion content.")

    def test_discussion_list_view(self):
        """
        Test that the discussion list view returns a 200 status code and uses the correct template.
        Adjust the 'discussion:list' URL name to match your URL configuration.
        """
        response = self.client.get(reverse('discussion:list'))
        self.assertEqual(response.status_code, 200)
        # Optionally, check that expected content is found in the response.
        self.assertContains(response, "Test Discussion")

    def test_discussion_detail_view(self):
        """
        Test that the discussion detail view displays the correct discussion.
        Adjust the URL name 'discussion:detail' and keyword arguments based on your configuration.
        """
        url = reverse('discussion:detail', kwargs={'pk': self.discussion.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Discussion")
        self.assertContains(response, "This is a test discussion content.")

    def test_invalid_url_returns_404(self):
        """
        Test that an invalid URL returns a 404 status.
        """
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)

    def test_create_discussion(self):
        """
        Test that a new discussion can be created via a POST request.
        Adjust the URL name and field names as per your form/view.
        """
        data = {
            'title': 'Another Discussion',
            'content': 'Content for another discussion.'
        }
        response = self.client.post(reverse('discussion:create'), data)
        # Check that the response redirects (assuming a successful POST redirects)
        self.assertIn(response.status_code, [302, 200])
        # Verify that the discussion exists in the database.
        self.assertTrue(Discussion.objects.filter(title='Another Discussion').exists())
