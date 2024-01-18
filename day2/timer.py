def get_time():
	"""Prompts the user for a time input and returns it as a tuple of hours, minutes, and seconds."""
	user_input = input('Enter time (HH:MM:SS or MM:SS): ')
	user_input = user_input.split(':')

	print(user_input)


def main():
	get_time()


if __name__ == '__main__':
	main()
