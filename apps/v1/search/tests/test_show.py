from . import FAKE_MEDIA
from rest_framework import status
from rest_framework.test import APITestCase


class SearchshowTestCase(APITestCase):
    '''
    Test cases for searching show endpoint.
    '''

    def setUp(self) -> None:
        self.show = 'gotham'

    def test_search_show_valid(self):
        '''
        Test for correct querying of data.
        Checks whether data returned is in correct format.
        '''
        response = self.client.get(f'/api/v1/search/show/?query={self.show}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 0)

        if len(data) > 0:
            '''
            Testing for first item as the rest should be the same.
            Check if an item's content contains the correct keys.
            '''
            first_item: dict = data[0]
            keys = ['title', 'key_visual', 'imdb_id', 'release_year']

            for key in first_item.keys():
                self.assertIn(key, keys)

    def test_search_show_invalid(self):
        '''
        Test for when no query has been provided to the endpoint.
        Checks whether error returned is in correct format.
        '''
        response = self.client.get(f'/api/v1/search/show/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data.keys()), 1)
        self.assertEqual(list(data.keys())[0], 'detail')

    def test_search_show_not_get(self):
        '''
        Test for when a request other than GET is sent.
        Uses PUT to test but this should be more or less the same for other request types.
        '''
        response = self.client.put(f'/api/v1/search/show/?query={self.show}')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data.keys()), 1)
        self.assertEqual(list(data.keys())[0], 'detail')

    def test_search_fake_show(self):
        '''
        Test for when a query of show that does not exist in the database.
        Simple check if it returns an empty list: [].
        '''
        response = self.client.get(f'/api/v1/search/show/?query={FAKE_MEDIA}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertListEqual(data, [])
