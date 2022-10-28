import random


class Guest:
    def __init__(self, name: str, fav_song, money: float) -> None:
        self.name = name
        self.fav_song = fav_song
        self.money = money
        self.position = None
        return

    def pay_entry(self, entry_fee):
        self.money -= entry_fee

    def check_favourite_song(self, room):
        if self.fav_song in self.position.songs:
            return f"{self.name}: I'll try room {self.position.name}. Hey it has my favourite song... '{self.fav_song.title}, tra la la'"
        else:
            rand_song_index = random.randint(0, (len(room.songs)-1))
            return f"{self.name}: I'll try room {self.position.name}. They don't have my song in here. Guess I'll try {room.songs[rand_song_index]}"
