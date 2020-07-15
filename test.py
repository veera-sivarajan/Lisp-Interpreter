#This is strictly for testing purpose
dic = { "x": 1, "y": 2,} 
lis1 = ("Hi", "Bye")
lis2 = ("Lorane", "Yanny")
dic.update(zip(lis1, lis2))
#print(dic["x"])
string = ["quote" , "x", "10"] 
op, *args = string
#print("op: ", op)
#print("args: ", args)
lis = ["cond", [["predicate"], ["then do somehting 1"]], [["predicate2"], ["then do something 2"]]]

op, *args = lis
print(args[0])
