import time
import pygame as pg
from pathlib import Path

MUSIC_FOLDER = Path(__file__).parent.joinpath("music")


class MusicManager:

    def __init__(self):
        self.sound_enabled = False
        self.initialize_audio()
        self.volume = 0.4

    def play_enchanted_festival(self):
        self.play_song("enchanted_festival.ogg")

    def play_title_theme(self):
        self.play_song("title_theme.ogg")

    def play_cherry_hill(self):
        self.play_song("cherry_hill.ogg")

    def play_bonfire(self):
        self.play_song("bonfire.ogg")

    def play_castles(self):
        self.play_song("castles_of_fog_and_cherry_blossoms.ogg")

    def load_music(self, filename):
        """Load a song."""
        music_file = MUSIC_FOLDER.joinpath(filename)
        if not music_file.is_file():
            raise OSError(f"Music '{music_file}' not found")
        return pg.mixer.music.load(str(music_file))

    def play_song(self, filename):
        if self.sound_enabled:
            pg.mixer.music.fadeout(100)
            self.load_music(filename)
            pg.mixer.music.set_volume(self.volume)
            pg.mixer.music.play(-1)

    def stop_music(self):
        if self.sound_enabled:
            pg.mixer.music.fadeout(500)

    def initialize_audio(self):
        """Setup the audio system."""
        loop = 3
        while True:
            try:
                pg.mixer.init()
            except Exception:
                if loop <= 0:
                    print("WARNING: Unable to initialize audio system")
                    break
                else:
                    try:
                        pg.mixer.quit()
                    except Exception:
                        pass
                    time.sleep(1)
            else:
                self.sound_enabled = True
                break
            loop -= 1
