from os import system
system("Cls")
name1,name2,name3,name4,name5=(input(">>")),(input(">>")),(input("->")),(input("<<")),(input("+>"))
print(name1.replace(" ","...")) if" "in name1 else print(f"{name1}")
print(name2.lower())
print(name3.replace(":)","😁")) if":)"in name3 else print(f"{name3}")
print(name3.replace(":(","😕")) if":("in name4 else print(f"{name4}")
print(name5.replace(":|","😐")) if":|"in name5 else print(f"{name5}")