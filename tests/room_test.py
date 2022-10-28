import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Room trial", "Theme trial", 10)
        self.room1 = Room("room trial1", "theme trial1", 1)

        self.song1 = Song("500 miles", "The Proclaimers", "Easy")
        self.song2 = Song("Happy", "Pharrell Williams", "Easy")
        self.song3 = Song("Copacabana", "Barry Manilow", "Easy")
        self.song4 = Song("MMMBop", "Hanson", "Fun")
        self.song5 = Song("If You Like Pina Coladas", "Jimmy Buffet", "Fun")
        self.song6 = Song("Tubthumping", "Chumbawamba", "Fun")
        self.song7 = Song("Time of your life", "Greenday", "90s")
        self.song8 = Song("Getting jiggy with it", "Will Smith", "90s")
        self.song9 = Song("Don't speak", "No doubt", "90s")
        self.song10 = Song("I will always love you", "Whitney Houston", "Ballads")
        self.song11 = Song("Someone like you", "Adele", "Ballads")
        self.song12 = Song("My heart will go on", "Celine Dion", "Ballads")
        
        self.guest1 = Guest("Ron", self.song8, 100)
        self.guest2 = Guest("Harry", self.song5, 100)
        self.guest3 = Guest("Hermione", self.song11, 100)

    def test_room_has_name(self):
        self.assertEqual("Room trial", self.room.name)

    def test_room_has_theme(self):
        self.assertEqual("Theme trial", self.room.theme)

    def test_room_has_cap(self):
        self.assertEqual(10, self.room.capacity)
        return

    def test_room_add_song(self):
        self.room.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room.songs))
        return

    def test_check_capacity(self):
        self.room1.add_guest_to_room(self.guest1, self.room1)
        self.assertEqual(False, self.room1.check_capacity())
        self.assertEqual(True, self.room.check_capacity())

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest1, self.room)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(self.room, self.guest1.position)
        return
    
    def test_add_guest_to_room(self):
        self.room.add_song_to_room(self.song8)
        self.room.add_guest_to_room(self.guest1, self.room)
        self.assertEqual(self.room, self.guest1.position)

    def test_room_remove_guest(self):
        self.room.add_guest_to_room(self.guest1, self.room)
        self.room.remove_guest_from_room(self.guest1)
        self.assertEqual(0, len(self.room.guests))
        return

    def test_print_things(self):
        pass
        # print(self.guest2.fav_song.title)
