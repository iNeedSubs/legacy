from . import FAKE_MEDIA
from rest_framework import status
from rest_framework.test import APITestCase


class SearchMovieTestCase(APITestCase):
    '''
    Test cases for searching movie endpoint.
    '''

    def setUp(self) -> None:
        self.movie = 'the dark knight'
        self.base_url = '/api/v1/search/movie?query='

    def test_search_valid(self):
        '''
        Test for correct querying of data.
        Checks whether data returned is in correct format.
        '''
        response = self.client.get(f'{self.base_url}{self.movie}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 0)

        if len(data) > 0:
            '''
            Check if an item's content contains the correct keys.
            Testing for first item as the rest should be the same.
            '''
            first_item: dict = data[0]
            keys = ['title', 'poster', 'banner', 'imdb_id', 'release_date']

            self.assertEqual(len(first_item.keys()), len(keys))

            for key in first_item.keys():
                self.assertIn(key, keys)
                if key == 'imdb_id':
                    self.assertNotIn(key, [None, ''])

            # No items in the list should return None
            self.assertFalse(None in data)

    def test_search_invalid(self):
        '''
        Test for when no query has been provided to the endpoint.
        Checks whether error returned is in correct format.
        '''
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data.keys()), 1)
        self.assertEqual(list(data.keys())[0], 'detail')

    def test_search_not_get(self):
        '''
        Test for when a request other than GET is sent.
        Uses PUT to test but this should be more or less the same for other request types.
        '''
        response = self.client.put(f'{self.base_url}{self.movie}')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data.keys()), 1)
        self.assertEqual(list(data.keys())[0], 'detail')

    def test_search_fake(self):
        '''
        Test for when a query of movie that does not exist in the database.
        Simple check if it returns an empty list: [].
        '''
        response = self.client.get(f'{self.base_url}{FAKE_MEDIA}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertListEqual(data, [])
