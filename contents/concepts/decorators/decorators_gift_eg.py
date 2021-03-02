# def great_packer(fun):
# 	print("Hello Sir, Welecome to Great Packer.")
# 	def packer():
# 		print("I'm Packer, I'll pack your gift in 5min.\n")
# 		fun()
# 		print("Done. Thank youu! Come again")
# 	return packer


#1
# def gift():
# 	print("Okayy, Finally gift is getting packed.\n")


# gp = great_packer(gift)
# gp()


#2
# @great_packer
# def gift():
# 	print("Okayy, Finally gift is getting packed.\n")


#gift()

#======================================================================

def great_packer(fun):
	print("Hello Sir, Welecome to Great Packer.")
	def packer(name, message):
		print("I'm Packer, I'll pack your gift in 5min.\n")
		nm, msg = fun(name, message)
		print("\n\nDear {},\n\n{}.\n\n".format(nm, msg))
		print("Done. Thank youu! Come again")
	return packer


@great_packer
def gift(name, message):
	print("Okayy, Finally gift is getting packed.")
	return name, message

if __name__ == "__main__":
	name = input("name:\n")
	msg = input("message:\n")
	print("*********************************************")
	gft = gift(name, msg)
	print(gft)
	print("*********************************************")



#=====================================================================


# def add(fun):
# 	def inner(a, b):
# 		print("add a and b")
# 		ai, bi = fun(a, b)
# 		return ai+bi
# 	return inner

# def ab(a, b):
# 	return a, b

# a, b = 10, 20
# add_obj = add(ab)
# res=add_obj(a, b)
# print(res)


# @add
# def ab(a, b):
# 	return a, b

# print(ab(10, 20))
