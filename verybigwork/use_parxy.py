def use():
	import random
	with open("succ_pond.txt","r",encoding="utf-8") as f:
		content = f.readlines()
	try:
		res = content.pop(0)
	except:
		res = "none"
	with open("succ_pond.txt","w",encoding="utf-8") as f:
		f.write("".join(content))
	return res.strip()
