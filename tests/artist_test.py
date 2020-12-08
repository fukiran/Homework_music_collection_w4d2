import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist('Lee Perry')

    def test_artist_has_name(self):
        self.assertEqual('Lee Perry',self.artist.name)
