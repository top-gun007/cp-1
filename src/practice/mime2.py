# http://www.codechef.com/problems/MIME2

# This one seems easy considering it's just strings.
# Just using a dictionary should work.

input_arr = map(int, raw_input().split())
num_types = input_arr[0] # This is not memory efficient in any manner.
num_files = input_arr[1]
type_dict = {}
for i in range(0, num_types):
	input_arr = raw_input().split()
	extension = input_arr[0] # Not even trying to save memory now, lol
	filetype = input_arr[1]
	if not filetype in type_dict:
		type_dict[filetype] = [extension]
	else:
		type_dict[filetype].extend(extension)


def find_filetype(filename):
	''' 
	This function finds the extension from the filename and then returns 
	the appropriate filetype from type_dict. Returns "unknown" if filename
	does not have an extension or if extension is not present in type_dict.
	'''
	if not '.' in filename: 
		return "unknown"
	else:
		extension = ""
		for ch in filename[::-1]:
			if ch == '.':
				break
			else:
				extension = ch + extension
		for t in type_dict:
			if extension in type_dict[t]:
				return t
		return "unknown"
		

for i in range(0, num_files):
	# Was getting lots of wrong answers before I read the comments.
	# Apparently if a file has a space, Codechef wants you to check for the 
	# extension from the left of the space and not from the end.
	# Weird.
	filename = raw_input().split()[0] 
	print find_filetype(filename)