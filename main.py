import os, time, openhello, lvls
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
cls()
if os.path.exists("./profile") != True:
	openhello.load()
else:
	load_lvl_num = open('./profile/LVL.mg', 'r').read()
	cls()
	print("Загрузка", load_lvl_num, "эпизода игры")
	lvls.lvl(int(load_lvl_num))
	