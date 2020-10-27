from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestRobotsTxt(TestCase):

    def test_get(self):
        '''
        Test if the response returned is what we expect from a GET request.
        '''
        response = self.client.get(reverse('robots:txt'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['content-type'], 'text/plain')

        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], 'User-Agent: *')

    def test_post_disallowed(self):
        '''
        Test if the response returned from a disallowed request method
        returns the appropriate status code.
        '''
        response = self.client.post(reverse('robots:txt'))
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_alias_url(self):
        '''
        Test if the alias url redirects the user back to the correct url.
        '''
        response = self.client.get(reverse('robots:alias'))
        self.assertRedirects(
            response=response,
            expected_url=reverse('robots:txt'),
            status_code=status.HTTP_302_FOUND,
            target_status_code=status.HTTP_200_OK,
            fetch_redirect_response=False
        )
