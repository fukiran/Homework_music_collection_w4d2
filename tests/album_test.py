import unittest
from models.album import Album 


class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album('Black Ark', 'dub', 'Lee Perry')

    def test_album_has_title(self):
        self.assertEqual('Black Ark',self.album.title)

    def test_album_has_genre(self):
        self.assertEqual('dub', self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual('Lee Perry', self.album.artist)