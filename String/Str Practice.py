 # 1
txt=input("Razo")
txt=txt.replace("R" , "1")
txt=txt.replace("r" , "1")
print(txt)





# 2
txt=input("Razo")
txt=txt.replace("a" , "1")
txt=txt.replace("e" , "2")
txt=txt.replace("i" , "3") 
txt=txt.replace("o" , "4")
txt=txt.replace("u" , "5")
print(txt)



# # 3
tiv=int(input("Tiv: "))
if tiv>=0 and tiv<=3:
	print("0-3")
elif tiv> 3 and tiv<=5:
	print("3-5")
elif tiv>5 and tiv<=10:
	print("5-10")
else:
 	print("mijakayqum chi!  ")




# # 4
 text='vvvvvv'
if text.count("v")>3:
	print("mec e 3ic")
elif text.count("s"):
	print("s eri qanaky", text.count"s")
else:
	print("v chka" , "s chka")



# # 5
anun="Rob"
if anun== "Rob":
	print("Rob")
elif anun=="Raffi":
	print("Raffi")
else:
	print("voch rob e voch raffi")



# 6
bar="bareev"
print("bar: " + bar)
tar="e"
print("tar:  "  + tar)
if bar.find(tar) != -1:
	print(bar.find(tar))
else:
	print("tary texti mej chi")


