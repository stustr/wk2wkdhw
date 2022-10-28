import unittest

from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self) -> None:
        self.guest1 = Guest("Ron", "Dance", 5)
        return
    
    def test_kb_has_name(self):
        self.assertEqual("Ron", self.guest1.name)
        return
        
    def test_guest_has_fav_song(self):
        self.assertEqual("Dance", self.guest1.fav_song)
        return
    
    def test_guest_has_money(self):
        self.assertEqual(5, self.guest1.money)
        return