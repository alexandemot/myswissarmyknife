
from os import system, name


class colors:
	HEADER    = '\033[95m'
	BLUE      = '\033[94m'
	GREEN     = '\033[92m'
	WARNING   = '\033[93m'
	FAIL 	  = '\033[91m'    
	BOLD 	  = '\033[1m'
	UNDERLINE = '\033[4m'
	CLEANUP	  = '\033[0m'
	
	

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')

clear()