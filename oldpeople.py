from random import *


#Create the list of words you want to choose from.
dad_list = ["Tony","Bert","Walter","Richard","Edward","Howard","Larry"]
mom_list = ["Patty","Mary","Kathy","Linda","Mary-Ann","Shannon","Michele"]
oldpeople_list = [dad_list,mom_list]
#Generates a random integer.
x = randint(0, len(dad_list)-1) 
y = randint(0, len(mom_list)-1)
print (dad_list[x])
print (mom_list[y])
def Onlist(mom_list):
 for item in mom_list:
  print(item)
Onlist(dad_list)
Onlist(mom_list)	
