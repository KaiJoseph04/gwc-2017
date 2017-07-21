class User:
# Define the fields and methods for your object here.
	def __init__(self, newUsername, newUserID):
		self.username = newUsername
		self.userID = newUserID
		self.friends = []

	def getUserName(self):
		return self.username

	def getUserID(self):
		return self.userID

	def getFriends(self):
		return self.friends

	def addFriends(slfef, friendID):
		self.friends.appened(friendID)

class Network:
	def __init__(self):
		self.users=[]
	def numUser(self):
		return len(self.users)
	def addUser(Self, username):
		self.users.append(User(username, user-ID))

	def getUserID(self, username):
		for user in self.users:
			if username==user.getUserName():
				user_id=user.getUserID()
			return user-id
	def addConnection(self, user1, user2):
		user1_id=self.getUserID(user1)
		user2_id=self.getUserID(user2)

		user1=self.users[user1_id]
		user2=self.users[user2_id]

		self.users[user2_id].addFriends(user1_id)
		self.users[user1_id].addFriends(user2_id)
	def printUsers(self):
		print("this is the Network")
		for user in self.users:
			print("\tUser {}: {}".format(user.getUserID, user.getUserName))



def main():
# Define the program flow for your user interface here.
	mynetwork=Network()
	done=False
	while not done:
		action=input("\nWhat would you like to do ?Add a user(u) , Add a connection (c), Print Friend List (p),Exit (e)")
		if action=="u":
			username=input("What username?")
			mynetwork.adduser(username)
		elif action=="c":
			if mynetwork.numUsers()<2:
				print("ERROR. Dont have enough users.")
				continue
			else:
				user1=input("First User?")
				user2=imput("SecondUser?")
				mynetwork.addConnection(user1,user2)
		elif action=="p":
			mynetwork.printUsers()
		elif action=="e":
			print("Come back soon)-:")
			done=True
		else:
			print("ERROR.Sorry, I dont understand")










# Runs your program.
if __name__ == '__main__':
	main()
