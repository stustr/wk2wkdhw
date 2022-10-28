class Room:
    def __init__(self, name: str, theme: str, capacity: int) -> None:
        self.name = name
        self.theme = theme
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def add_song_to_room(self, song):
        self.songs.append(song)

    def check_capacity(self):
        return len(self.guests) < self.capacity

    def add_guest_to_room(self, guest, room):
        if self.check_capacity():
            self.guests.append(guest)
            guest.position = room
            print(guest.check_favourite_song())

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)
