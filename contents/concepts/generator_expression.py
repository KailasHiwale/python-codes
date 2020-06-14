if __name__ == '__main__':
	je_obj = (line for line in open('./fileIO/iofile/blg.txt'))
	# import ipdb;ipdb.set_trace()

# Output
ipdb> je_obj.__next__()                                                                                                                              
'Register:\n'
ipdb> je_obj.__next__()                                                                                                                              
'-first_name\n'
ipdb> je_obj.__next__()                                                                                                                              
'-last_name\n'
ipdb> je_obj.__next__()                                                                                                                              
*** StopIteration
