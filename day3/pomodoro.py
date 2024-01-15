import time as time_module
from datetime import datetime
from datetime import timedelta
import os, argparse


def get_positive_int_input(prompt):
    """Prompts the user for a positive integer input until a valid one is provided."""
    
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print('Please enter a positive integer.')    
        except ValueError:
            print("Sorry, I didn't understand that.")


def format_time(minutes, seconds):
    """Formats the given minutes and seconds as a string in the format 'MM min, SS sec'."""
    
    return f'{minutes:02d} min, {seconds:02d} sec'


def pomodoro(pomo_length):
    """Runs a Pomodoro timer for a user-specified number of minutes."""

    if pomo_length is None:
        pomo_length = get_positive_int_input('Enter the session time in minute(s): ')
    pomo_end = datetime.today() + timedelta(minutes=pomo_length)

    while True:
        time_left = max(0, (pomo_end - datetime.today()).total_seconds())
        
        if time_left == 0:
            break

        minutes_left, seconds_left = divmod(int(time_left), 60)
        print(f'\r{format_time(minutes_left, seconds_left)}', end='', flush=True)
        
        time_module.sleep(1)
    
    print('\nYay, your pomodoro sessios is over!')
    os.system('afplay /System/Library/Sounds/Ping.aiff')


def main():
    """Main function that parses command-line arguments and runs the Pomodoro timer."""
    
    parser = argparse.ArgumentParser(description='Pomodoro timer application.')
    parser.add_argument('-t', '--time', type=int, help='The length of the Pomodoro session in minutes.')
    args = parser.parse_args()

    print('---=== Pomodoro App ===---')
    pomodoro(args.time)


if __name__ == '__main__':
    main()
