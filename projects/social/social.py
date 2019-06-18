import sys
sys.path.append(sys.path[0]+"\\..\\graph")

from random import randint
from util import Queue

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # create all the users
        for i in range(numUsers):
            # in future make name
            self.addUser(i)

        total_friendships = numUsers * avgFriendships / 2
        # do check to see if this is over half the users. If so throw error
        # create freinds between users
        # keep track of made friends
        friendships = [(None, None)]
        while total_friendships > 0:
            # grab two random user ids
            friend1 = None
            friend2 = None
            while friend1 == friend2 or  (friend1, friend2) in friendships or (friend2, friend1) in friendships:
                friend1 = randint(1, numUsers )
                friend2 = randint(1, numUsers )
            # make the friendship
            self.addFriendship(friend1, friend2)
            # add friendship to created
            friendships.append((friend1, friend2))
            # reduce number of friends to make
            total_friendships -= 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        # user and path to user
        q.enqueue([userID, []])
        
        while q.size() > 0:
            item = q.dequeue()
            currentUserID = item[0]
            path = item[1]
            if currentUserID not in visited:
                visited[currentUserID] = path
                for next_user in self.friendships[currentUserID]:
                    new_path = path.copy()
                    new_path.append(currentUserID)
                    q.enqueue([next_user, new_path])
        # del own 
        del visited[userID]
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
