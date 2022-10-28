from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

the_bar = KaraokeBar("Dumble's Disco", 500.00, 5.50)

rooms = [
    Room("One", "Easy", 10),
    Room("Two", "Fun", 1),
    Room("Three", "90s", 1),
    Room("Four", "Ballads", 1),
]

""" song1 = Song("500 miles", "The Proclaimers", "Easy")
song2 = Song("Happy", "Pharrell Williams", "Easy")
song3 = Song("Copacabana", "Barry Manilow", "Easy")
song4 = Song("MMMBop", "Hanson", "Fun")
song5 = Song("If You Like Pina Coladas", "Jimmy Buffet", "Fun")
song6 = Song("Tubthumping", "Chumbawamba", "Fun")
song7 = Song("Time of your life", "Greenday", "90s")
song8 = Song("Getting jiggy with it", "Will Smith", "90s")
song9 = Song("Don't speak", "No doubt", "90s")
song10 = Song("I will always love you", "Whitney Houston", "Ballads")
song11 = Song("Someone like you", "Adele", "Ballads")
song12 = Song("My heart will go on", "Celine Dion", "Ballads")

songs = [
    song1,
    song2,
    song3,
    song4,
    song5,
    song6,
    song7,
    song8,
    song9,
    song10,
    song11,
    song12,
] """

songs = [
    Song("500 miles", "The Proclaimers", "Easy"),
    Song("Happy", "Pharrell Williams", "Easy"),
    Song("Copacabana", "Barry Manilow", "Easy"),
    Song("MMMBop", "Hanson", "Fun"),
    Song("If You Like Pina Coladas", "Jimmy Buffet", "Fun"),
    Song("Tubthumping", "Chumbawamba", "Fun"),
    Song("Time of your life", "Greenday", "90s"),
    Song("Getting jiggy with it", "Will Smith", "90s"),
    Song("Don't speak", "No doubt", "90s"),
    Song("I will always love you", "Whitney Houston", "Ballads"),
    Song("Someone like you", "Adele", "Ballads"),
    Song("My heart will go on", "Celine Dion", "Ballads"),
]

guests = [
    Guest("Ron", songs[7], 100),
    Guest("Harry", songs[5], 100),
    Guest("Hermione", songs[11], 100),
]

[
    room.add_song_to_room(song)
    for room in rooms
    for song in songs
    if song.theme == room.theme
]

[print(room.name, room.songs) for room in rooms]
