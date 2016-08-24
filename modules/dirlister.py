import os
def run(**args):
	print "[*] in dirlister modeule."
	files = os.listdir(".")
	return str(files)