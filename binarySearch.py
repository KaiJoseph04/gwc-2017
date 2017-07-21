print("Starting search")
def find(alphabet,target):  
	print("calling the function")
	top = 0
	bottom = len(alphabet) - 1
	while (top<=bottom):
		middle = (top + bottom)//2
		midpoint = alphabet[middle]
		print("Top",top,"Bottom",bottom,"Middle",middle)
		if midpoint > target:
			bottom = middle - 1
			print ("going left")
		if midpoint < target:
			top = middle + 1
			print ("going right")
		if midpoint==target:
			print("here is the letter you are looking for")			
			break
alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
"l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
find(alphabet, "g")
