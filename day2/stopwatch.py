from datetime import datetime
import time as time_module
import threading

stop = False


def format_time(minutes, seconds):
	"""Formats the given minutes and seconds as a string in the format 'MM min, SS sec'."""

	return f'{minutes:02d} min, {seconds:02d} sec'


def wait_for_enter():
	"""Waits for the user to press Enter."""

	print('Press Enter to stop...')
	global stop
	input()
	stop = True


def timer():
	"""Starts a timer and continuously prints the elapsed time to the console."""
	
	start_time = datetime.today()
	while not stop:
		time_elapsed = (datetime.today() - start_time).total_seconds()
		minutes, seconds = divmod(int(time_elapsed), 60)
		print(f'\r{format_time(minutes, seconds)}', end='', flush=True)
		time_module.sleep(1)


def main():
	# Start the thread that waits for user input
	threading.Thread(target=wait_for_enter).start()
	
	# Start the timer
	timer()


if __name__ == '__main__':
	main()
