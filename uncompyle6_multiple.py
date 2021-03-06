'''
Maxwell Dulin 
While attempting to exploit a NAS device, I figured out that the NAS was running the webserver based upon pyc files. So, I decided to just use uncompyle6 to get the python source code back for all of the files. The scipt below is how I did it.
'''


import os

'''
Traverses through the entire directory structure to convert all pyc files in py files with uncompyle6. 

Args: 
	directory: The location where the traverse is happening. 
	option: Two options: 
		True: Convert all of the pyc files to py files 
		False: Remove all of the pyc files in the directory
'''
def traverse_change(directory = './', option = True):
	rootdir = directory
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			total_file = os.path.join(subdir, file)
			if('.pyc' in total_file):
				# Convert all the pyc files to py files. 
				if(option == True):
					print('Starting...', total_file)
					convert_file(total_file) 
					print('Finishing...', total_file)
				# Remove all .pyc files in the new directory
				elif(option == False): 
					print('Removing...', total_file)
					cmd = 'rm ' + total_file 
					os.system(cmd) 
				
'''
Converts a file from a .pyc into a py file, assuming that uncompyle6 is installed. 

Args: 
	file_name: the full path of the file to convert 
Returns: 
	Nothing 
'''			
def convert_file(file_name): 
	cmd = 'uncompyle6 ' + file_name
	cmd += ' >> ' + file_name[0:-1]
	os.system(cmd) 
	return 

'''
Moves all of the files into a new directory, while removing all of the pyc files.

Args: 
	new_location: The location to place the new files at. 
'''
def move_files(new_location): 
	cmd = 'cp -r ./ ' + new_location
	os.system(cmd) 	
	traverse_change(new_location, False)

traverse_change() 
