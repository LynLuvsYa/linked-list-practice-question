# 9618/41/M/J/21

# further subroutine, remove an item of data


#classes + definitions
class node: # turning "nodes" into a data type
    def __init__(self):
        data = 0
        nextNode = 0

        
def pr(): # a nice way of printing the data and its link
    for x in range(9):
        print(linkedList[x].data, "|", linkedList[x].nextNode)

    
def outputnodes(startPointer): #printing the data in order of the links, and stopping at -1, rather than printing in order of the arraya and finishing at the end of it.
    pointer = startPointer
    while pointer != -1: # while it's not the end of the linked list, print the data in order of the links.
        print(linkedLins[pointer].data)
        pointer = linkedList[pointer].nextNode


def empty(): # checks where the next free position is.
    for x in range(9):
        if linkedList[x].data == 0 and linkedList[x].nextNode != -1:
            return x
    return -1 # returns -1 if the data is full


def addNode(data):
    global emptylist
    if emptylist == -1: return False # if it's full, return False

    pointer = 1
    
    for x in range(len(linkedList)):
        pointer = linkedList[pointer].nextNode #
        if pointer == -1:
            pointer = temp
            break
        temp = pointer
    
    linkedList[pointer].nextNode = emptylist #the previous -1 pointer now becomes the next free position's index
    linkedList[emptylist].data = data # add the data into that spot
    linkedList[emptylist].nextNode = -1 # change that to the end of the list
    
    return True


def removenode(pos): # as the name states, it removes the position specified by the user
    
    for x in range(9):
        if linkedList[x].nextNode == pos: # if it's pointing to the data you want to remove
            linkedList[x].nextNode = linkedList[pos].nextNode # it now points to the data that the removed position was pointing to
            break
        
    linkedList[pos].data = 0 # empty data
    linkedList[pos].nextNode = pos + 1 # points to next index

    
#main (initialisation)
linkedList = []
tempdata = [1,5,6,7,2,0,0,56,0,0] #original data
tempNN = [1,4,7,-1,2,6,8,3,9,-1] # their respective links
emptylist = 5 # the next free position in the linked list.


#main (programming)
for x in range(9):
    linkedList.append(node()) #appends a blank space of data type "node"
    linkedList[x].data = tempdata[x] #that space's data = the data in the paper
    linkedList[x].nextNode = tempNN[x] # and its link

pr()
print("______")
outputnodes(0)

emptylist = empty()

addNode(
    int(input("input data to add: "))
    )

pr()
print("_______")    
outputnodes(0)
removenode(3)
print("______")
outputnodes(0)
