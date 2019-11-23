#https://www.geeksforgeeks.org/deque-in-python/

from collections import deque

search_queue = deque() #Creates a new queue
graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = ['Lara m']

search_queue += graph["you"]


def person_is_seller(name): 
    return name[-1] == 'm'

while search_queue: #While the queue isn’t empty ...
    person = search_queue.popleft() #... grabs the first person off the queue 
    if person_is_seller(person):         #Checks whether the person is a mango seller
        print (person + ' is a mango seller!')       #Yes, they’re a mango seller.
        #return True 
    else:
        search_queue += graph[person] #No, they aren’t. Add all of this 
    #return False