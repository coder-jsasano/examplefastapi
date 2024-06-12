#Alarm Clock
from playsound import playsound
import time

#ANSI = Manipulate the terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

#Alarm format
def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will go off in {minutes_left:02d}:{seconds_left:02d}")

    playsound('C:\\Users\\junpe\\Python code\\Tutorials\\Python Project\\Alarm_Rooster.mp3')


minutes = int(input('How many minutes to wait for the alarm?: '))
seconds = int(input("How many seconds to wait?: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)



