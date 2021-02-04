import os, time
def load():
	def loaloa(x):
		def cls():
			os.system('cls' if os.name=='nt' else 'clear')
		memshack_text = ["MEMSHACK CONSOLE GAME...", "Привет хацкер. Готов к квесту?","\nЕсли \"ДА\", то погнали!"]
		load_text = ""
		for load in range(len(memshack_text[x])):
			load_text += memshack_text[x][load]
			print(load_text)
			time.sleep(0.1)
			cls()
		print(load_text)
	for y in range(3):
		time.sleep(2)
		loaloa(y)
	name = input("Придумай себе ник@HackQ# ")
	os.system("mkdir ./profile")
	profile = open("./profile/GNAME.mg", "w+")
	profile.write(str(name))
	profile = open("./profile/LVL.mg", "w+")
	profile.write("1")
	profile.close()
	print("Пора начинать", name, "!")
	time.sleep(2)
	os.system("./start")

