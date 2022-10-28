class Song:
    def __init__(self, title:str, artist:str, theme:str) -> None:
        self.title = title
        self.artist = artist
        self.theme = theme
        return
    
    def __repr__(self) -> str:
        return f"{self.title} by {self.artist}"