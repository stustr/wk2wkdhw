class Guest:
    def __init__(self, name: str, fav_song, money: float) -> None:
        self.name = name
        self.fav_song = fav_song
        self.money = money
        self.position = None
        return

    def pay_entry(self, entry_fee):
        self.money -= entry_fee

    def check_favourite_song(self):
        if self.fav_song in self.position.songs:
            return "This room has my favourite song"
        else:
            return "They don't have my song in here"
