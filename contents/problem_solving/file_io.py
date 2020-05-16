import os


def count_line(file):
	count = 0
	with open(file) as file:
		for line in file:
			count+=1
	return count


def dirs_files_count(dir_path):
	file_count, dir_count = 0, 0
	for root, dirs, files in os.walk("iofile/"):
		file_count += len(files)
		dir_count += len(dirs)
	print("Number of files: {} \nNumber of directories: {}".format(file_count, dir_count))


if __name__ == '__main__':
	# count_line("blg.txt")
	dirs_files_count("iofile/")