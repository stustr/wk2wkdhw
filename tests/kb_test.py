import unittest

from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest

class TestKB(unittest.TestCase):
    def setUp(self) -> None:
        self.karaoke_bar = KaraokeBar("KB", 100, 10)
        self.room = Room("Room trial", "theme trial", 2)
        self.guest = Guest('guest trial', 'song trial', 100)
        return
    
    def test_kb_has_name(self):
        self.assertEqual("KB", self.karaoke_bar.name)
        return
    
    def test_kb_has_till(self):
        self.assertEqual(100, self.karaoke_bar.till)
        return
    
    def test_kb_has_entry_fee(self):
        self.assertEqual(10, self.karaoke_bar.entry_fee)
        return
    
    def test_kb_add_room(self):
        self.karaoke_bar.add_rooms(self.room)
        self.assertEqual(1, len(self.karaoke_bar.rooms))
        return
    
    def test_guest_entry(self):
        self.karaoke_bar.guest_entry(self.guest)
        self.assertEqual(110, self.karaoke_bar.till)
        self.assertEqual(90, self.guest.money)
        return