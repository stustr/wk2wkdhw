class KaraokeBar:
    def __init__(self, name, till, entry_fee) -> None:
        self.name = name
        self.rooms = []
        self.till = till
        self.entry_fee = entry_fee
        return

    def add_rooms(self, room):
        self.rooms.append(room)
        return
    
    def guest_entry(self, guest):
        self.till += self.entry_fee
        guest.pay_entry(self.entry_fee)