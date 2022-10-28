import random
from src.guest import Guest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.song import Song

the_bar = KaraokeBar("Dumble's Disco", 500.00, 5.50)

rooms = [
    Room("One", "Easy", 2),
    Room("Two", "Fun", 2),
    Room("Three", "90s", 2),
    Room("Four", "Ballads", 2),
]

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
    Guest("Harry", songs[4], 100),
    Guest("Hermione", songs[10], 100),
]

[
    room.add_song_to_room(song)
    for room in rooms
    for song in songs
    if song.theme == room.theme
]


print(f"\nWelcome to {the_bar.name}!\n")

[print(the_bar.guest_entry(guest)) for guest in guests]
print("")

for guest in guests:
    rand_room = rooms[random.randint(0, (len(rooms) - 1))]
    print(rand_room.add_guest_to_room(guest, rand_room))
print("")

[print(room.remove_guest_from_room(guest)) for room in rooms for guest in room.guests]
[print(room.remove_guest_from_room(guest)) for room in rooms for guest in room.guests]
print("")

print(f"Ron: Any fancy a duet?")
rand_dueter = guests[random.randint(1, 2)]
print(f"{rand_dueter.name}: Come on then.")
print("")

print(
    f"Ron & {rand_dueter.name}: 'Islands in the stream, that is what we are, and we rely on each other, ahhaaaaaa!"
)
if rand_dueter.name == "Harry":
    print("Hermione: Oh no!!!")
else:
    print("Harry: Oh no!!!!")

print("\n\n")
print("                                 FIN")
print("\n\n\n")
