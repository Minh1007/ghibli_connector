from django.test import TestCase
from django.urls import reverse


class MoviesInfoTest(TestCase):

    def setUp(self):
        self.api_endpoint = reverse('Movies-list')
        super().setUp()

    def test_get_user_info(self):
        """Test to get the movies
        """
        resp = self.client.get(self.api_endpoint)
        self.assertEqual(resp.status_code, 200)
