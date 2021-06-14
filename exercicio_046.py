import time
import emoji

x = len("Contagem regressiva para estouro de fogos de artifício")
print("*" * x)
print("Contagem regressiva para estouro de fogos de artifício")
print("*" * x)

#n=10
for count in range(10,-1,-1): # pode colocar range (0,11,1)
	print(count)
	#n = n - 1
	time.sleep(1)

#print(emoji.emojize(":boom:", use_aliases=True))
print(emoji.emojize("\n\033[1;31m:boom:\033[m \033[1;33m:boom:\033[m \033[1;36m:boom:\033[m :boom:", use_aliases=True))

#print ("\033[1;31mBBuummmm !!!!\033[m   \033[1;33mBBBBuummm !!!!\033[m   \033[1;36mBBBBuummmm !!!!\033[m  BBBBBBuuummmm !!!! ")
