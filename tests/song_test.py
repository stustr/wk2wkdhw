import unittest

from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self) -> None:
        self.song = Song("SongTrial", 'Artist trial', 'Theme trial')

    def test_song_has_title(self):
        self.assertEqual("SongTrial", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Artist trial", self.song.artist)
    
    def test_song_has_theme(self):
        self.assertEqual("Theme trial", self.song.theme)
