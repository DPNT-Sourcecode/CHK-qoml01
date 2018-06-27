import sys
from runner.user_input_action import get_user_input

if __name__ == '__main__':	
	i = get_user_input(sys.argv[1:])
	print i