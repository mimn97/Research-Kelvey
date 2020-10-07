
# # Scheme
# 1. There are a total of three big situations (6 subcases) in which each two players can possibly walk down edges in a given cube.
# 2. Using if-statements/switch statement, we will figure out the winning path that each player could take on
# 3. If it contains a vertex that already exists in the list of a player, then a loop is formed.

# Set a setting for simulating a cube by using 3D space (xyz-axis)
# mode 3: computer vs computer

import random

class GraphGame(object):
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.nodeList = [] # Initialization

    def addEdge(self,v1,v2):
        if v1 == v2:
            print("Same vertex %d and %d" %(v1, v2))
        else:
            if (str(v1) not in self.nodeList) and (str(v2) not in self.nodeList):
                self.nodeList.append(str(v1))
                self.nodeList.append(str(v2)) # Create a list for containing nodes in a given graph

            self.adjMatrix[v1-1][v2-1] = 1
            self.adjMatrix[v2-1][v1-1] = 1

    def removeEdge(self,v1,v2):
        if self.adjMatrix[v1-1][v2-1] == 0:
            print("No edge between %d and %d" %(v1, v2))
            return
        self.adjMatrix[v1-1][v2-1] = 0
        self.adjMatrix[v2-1][v1-1] = 0

    def isEdge(self,v1,v2):
        if self.adjMatrix[v1-1][v2-1] > 0:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def toString(self):
        i = 1
        for row in self.adjMatrix:
            print(i, row)
            i = i+1

    def gameOnGraph(self):

        p = []    # Total paths
        p1 = []   # Initialize Player 1 and Player 2 using list
        p2 = []

        comp = [] # Intialize the computer's choices and the user's choices
        user = []

        p1_adj = [] # Show nodes that player 1 can go to
        p2_adj = []

        comp_adj = []
        user_adj = []

        loop = [] # Show possible loop that could be made

        p.append("1") # Assumption: Player 1 always starts on the node [0,0,0]
        p1.append("1")


        #choice_p2 = "1" # Initialize it to 1
        #choice_comp = "1"

        count = 0

        print("\nGAME ON GRAPH \nFor the Relation Making Game, we assume that player 1 always starts first at the vertice 1 [0,0,0].")

        mode = input("Mode 1: 2 players \nGame 2: User vs Computer \nChoose Game mode: ")
        if mode == "1":
            print("Mode 1: 2 players")

            while (True):

                print("Path of p1: ", p1) # Show the list of nodes that p1 has already walked on
                print("Path of p2: ", p2) # Show the list of nodes that p2 has already walked on

                #print ("Total Path: ", p) # Show the list of all the nodes that both players have walked on

                for node in self.nodeList:
                    if count == 0: # For p2, this only applies to only the initial position
                        if self.adjMatrix[int(p[-1])-1][int(node)-1] == 1:
                            p2_adj.append(node)
                    else:
                        if self.isEdge(int(p[-1]), int(node)) and (p[-2] != node):
                            p2_adj.append(node)

                print("Possible vertices for p2 to go: ", p2_adj)

                for node in p2_adj:
                    if node in p:
                        loop.append(node)

                print("Any vertices that make a loop: ", loop)

                choice_p2 = input("\nLook at the list of vertices on a cube above. Which vertice can Player 2 go to? ")
                p2_adj.clear()
                loop.clear()

                count = 1 # Now, we can apply the general rule for both players to show the possible nodes that each can go to

                print("\n")
                if (choice_p2 in p):
                    print("RESULT\nPlayer 2 wins the game!\n")
                    break
                else:
                    p2.append(self.nodeList[int(choice_p2)-1])
                    p.append(self.nodeList[int(choice_p2)-1])

                    print("Current Path of p1: ", p1)
                    print("Current Path of p2: ", p2)
                    #print("Total Path: ", p)

                    for node in self.nodeList:
                        if self.isEdge(int(p[-1]), int(node)) and (p[-2] != node):
                            p1_adj.append(node)

                    print("Possible vertices for p1 to go: ", p1_adj)

                    for node in p1_adj:
                        if node in p:
                            loop.append(node)

                    print("Any vertices that make a loop: ", loop)
                    choice_p1 = str(input("\nLook at the list of vertices on a cube above. Which vertice can Player 1 go to? "))
                    p1_adj.clear()
                    loop.clear()

                    if (choice_p1 in p):
                        print("RESULT \nPlayer 1 wins the game!\n")
                        break
                    else:
                        p1.append(self.nodeList[int(choice_p1)-1])
                        p.append(self.nodeList[int(choice_p1)-1])

        elif mode == "2":
            # Assumption: User always starts on the node [0,0,0]
            user.append("1")
            print("\nMode 2: User vs. Computer")

            while (True): # For each trial, there are a total of 9 vertices that two players can access on.

                print("Path of Computer: ", comp) # Show the list of nodes that p1 has already walked on -> p2
                print("Path of User: ", user) # Show the list of nodes that p2 has already walked on -> p1

                print ("Total Path: ", p) # Show the list of all the nodes that both players have walked on

                for node in self.nodeList:
                    if count == 0: # For p2, this only applies to only the initial position
                        if self.adjMatrix[int(p[-1])-1][int(node)-1] == 1:
                            comp_adj.append(node)
                    else:
                        if self.isEdge(int(p[-1]), int(node)) and (p[-2] != node):
                            comp_adj.append(node)

                print("Possible vertices for computer to go: ", comp_adj)

                for node in comp_adj:
                    if node in p:
                        loop.append(node)

                print("Any vertices that make a loop: ", loop)

                if len(loop) > 0:
                    choice_comp = random.choice(loop)
                else:
                    choice_comp = random.choice(comp_adj)
                print("The computer's choice is: ", choice_comp)
                comp_adj.clear()
                loop.clear()

                count = 1 # Now, we can apply the general rule for both players to show the possible nodes that each can go to

                print("\n")
                if (choice_comp in p):
                    print("RESULT\nComputer wins the game!\n")
                    break
                else:
                    comp.append(self.nodeList[int(choice_comp)-1])
                    p.append(self.nodeList[int(choice_comp)-1])

                    print("Current Path of Computer: ", comp)
                    print("Current Path of User: ", user)
                    print("Total Path: ", p)

                    for node in self.nodeList:
                        if self.isEdge(int(p[-1]), int(node)) and (p[-2] != node):
                            user_adj.append(node)

                    print("Possible vertices for User to go: ", user_adj)

                    for node in user_adj:
                        if node in p:
                            loop.append(node)

                    print("Any vertices that make a loop: ", loop)
                    choice_user = str(input("\nLook at the list of nodes on a cube above. Which node can User go to? "))
                    user_adj.clear()
                    loop.clear()

                    if (choice_user in p1):
                        print("RESULT \nUser wins the game!\n")
                        break
                    else:
                        user.append(self.nodeList[int(choice_user)-1])
                        p.append(self.nodeList[int(choice_user)-1])

        else:
            print("Invalid Game Mode has been received.")


def main():

    # Hypercube
    c = GraphGame(8) # c is a cube and 8 is the number of vertices on the cube -> Initialize a cube
    c.addEdge(1,2)
    c.addEdge(1,4)
    c.addEdge(1,5)
    c.addEdge(2,3)
    c.addEdge(2,6)
    c.addEdge(3,4)
    c.addEdge(3,7)
    c.addEdge(4,8)
    c.addEdge(5,6)
    c.addEdge(5,8)
    c.addEdge(6,7)
    c.addEdge(7,8)

    print("\nHere is the adjacency matrix for a cube.\n")
    c.toString() # Make an adjacency matrix for the constructed graph

    c.gameOnGraph() # Play a game with the constructed graph


if __name__ == '__main__':
   main()
