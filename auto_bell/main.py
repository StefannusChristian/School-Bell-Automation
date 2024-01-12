import pygame
import schedule
import os
import sys
from time import sleep
from datetime import datetime

class BellAutomation:
    def __init__(self):
        if getattr(sys, 'frozen', False):
           script_dir = os.path.dirname(sys.executable)
        else:
           script_dir = str(os.path.dirname(__file__))

        # Define the sound files relative to the script or executable directory
        self.regular_sound_files = {
            "06:59:59": os.path.join(script_dir, "sounds","Bel Tanda Masuk Kelas.mp3"),
            "07:08:59": os.path.join(script_dir, "sounds","Bel Jam Ke-1.mp3"),
            "07:44:59": os.path.join(script_dir, "sounds","Bel Jam Ke-2.mp3"),
            "08:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-3.mp3"),
            "09:14:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "09:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-4.mp3"),
            "10:14:59": os.path.join(script_dir, "sounds","Bel Jam Ke-5.mp3"),
            "10:59:59": os.path.join(script_dir, "sounds","Bel Jam Ke-6.mp3"),
            "11:44:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "12:14:59": os.path.join(script_dir, "sounds","Bel Jam Ke-7.mp3"),
            "12:59:59": os.path.join(script_dir, "sounds","Bel Jam Ke-8.mp3"),
            "13:44:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "13:59:59": os.path.join(script_dir, "sounds","Bel Jam Ke-9.mp3"),
            "14:44:59": os.path.join(script_dir, "sounds","Bel Jam Ke-10.mp3"),
            "15:29:59": os.path.join(script_dir, "sounds","Bel Pulang Sekolah.mp3"),
        }

        self.friday_sound_files = {
            "06:59:59": os.path.join(script_dir, "sounds","Bel Tanda Masuk Kelas.mp3"),
            "07:08:59": os.path.join(script_dir, "sounds","Bel Jam Ke-1.mp3"),
            "07:44:59": os.path.join(script_dir, "sounds","Bel Jam Ke-2.mp3"),
            "08:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-3.mp3"),
            "09:14:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "09:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-4.mp3"),
            "10:14:59": os.path.join(script_dir, "sounds","Bel Jam Ke-5.mp3"),
            "10:59:59": os.path.join(script_dir, "sounds","Bel Jam Ke-6.mp3"),
            "11:44:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "12:44:59": os.path.join(script_dir, "sounds","Bel Jam Ke-7.mp3"),
            "13:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-8.mp3"),
            "14:14:59": os.path.join(script_dir, "sounds","Bel Istirahat.mp3"),
            "14:29:59": os.path.join(script_dir, "sounds","Bel Jam Ke-9.mp3"),
            "15:14:59": os.path.join(script_dir, "sounds","Bel Jam Ke-10.mp3"),
            "15:59:59": os.path.join(script_dir, "sounds","Bel Pulang Sekolah.mp3"),
        }

        # Set the initial sound files based on the day of the week
        self.sound_files = self.friday_sound_files if self.is_friday() else self.regular_sound_files

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
        # Schedule the events
        for time_str, sound_file in self.sound_files.items():
            # Convert time to 24-hour format
            time_str_24hr = self.convert_to_24hr_format(time_str)
            schedule.every().day.at(time_str_24hr).do(self.play_sound, sound_file)

        while True:
            # Run pending scheduled events and sleep for 1 second
            schedule.run_pending()
            sleep(1)

if __name__ == '__main__':
    bell = BellAutomation()
    print("Script is starting")
    try:
        bell.run()
    except Exception as e:
        print(f"An error occurred: {e}")