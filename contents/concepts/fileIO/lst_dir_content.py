import os


def lst_dir_content(dpath):
	for cpath in os.listdir(dpath):
		sd_path = os.path.join(dpath, cpath)
		if os.path.isdir(sd_path):
			lst_dir_content(sd_path)
		else:
			print(sd_path)


if __name__ == '__main__':
	lst_dir_content('./iofile/')