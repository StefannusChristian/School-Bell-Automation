import pygame
import schedule
from time import sleep
from datetime import datetime
from sound_files import regular_sound_files, friday_sound_files

class BellAutomation:
    def convert_to_24hr_format(self, time_str: str):
        # Convert 24-hour format
        dt_obj = datetime.strptime(time_str, '%H:%M:%S')
        return dt_obj.strftime('%H:%M:%S')

    def is_friday(self):
        # Check if today is Friday (weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
        return datetime.now().weekday() == 4

    def play_sound(self, sound_file: str):
        # Initialize pygame mixer and play the specified sound file
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def run(self):
        # Check if today is Friday to determine the sound files
        sound_files = friday_sound_files if self.is_friday() else regular_sound_files

        # Schedule the events
        for time_str, sound_file in sound_files.items():
            # Convert time to 24-hour format
            time_str_24hr = self.convert_to_24hr_format(time_str)
            schedule.every().day.at(time_str_24hr).do(self.play_sound, sound_file)

        while True:
            # Run pending scheduled events and sleep for 1 second
            schedule.run_pending()
            sleep(1)