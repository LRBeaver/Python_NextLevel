__author__ = 'lyndsay.beaver'
"""
Simulation of Web App Architecture

Service: The Russian Peasant's Algorith

Architecture Include:

- App Computer (Modules)
- Database (--) --> Russian Peasant Algorithm
- Load Balancer (Algorithm)

- Memcache (LiveJournal - 2003)
    - set[key, value]
    - get(key) --> value
    - delete(key)


+-----+    +-----+    +-----+
| APP |    | APP |    | APP |
|  1  |    |  2  |    |  3  |
+-----+    +-----+    +-----+

"""

## How does a load balancer work?

## 1) Random
## 2) Looping
## 3) Load Based

## Import Servers (Modules)

import computer1
import computer2
import computer3

## List of Servers
SERVERS = [computer1, computer2, computer3]

#SERVERS = ['APP1', 'APP2', 'APP3']
#SERVERS = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7']
server_range = len(SERVERS)

## OPTION 1
# n = -1
# def get_server():
#     global n
#     n += 1
#     return SERVERS[n % len(SERVERS)]


# def cycle(iterable):
#     ## cycle('ABCD') --> A B C D A B C D A B C D
#     saved = []
#     for element in iterable:
#         yield element
#         saved.append(element)
#     while saved:
#         for element in saved:
#             yield element

## OPTION 2
# import itertools
# ## Infinite Loop Iterator
# cycle = itertools.cycle(SERVERS)
# def get_server():
#     global cycle
#     return cycle.next()

## This is the load balancer algorithm ...round and round
## OPTION 3

def get_server():
    def f():
        while True:
            i = SERVERS.pop(0)
            SERVERS.append(i)
            yield i
    return next(f())

## Testing Load which needs balancing

if __name__ == '__main__':
    from random import randint
    # simulate a number of requests with this loop
    for i in range(10):
        #: Generate some 'Requested' numbers
        #a = randint(5, 99)
        #b = randing(5, 99)
        z = randint(1, 3)
        a = [45, 85, 123, 14, 32, 66, 102][z%7]
        b = [54, 14, 32, 46, 2, 112, 76][z%7]

        ## Run the load balancer
        server = get_server()

        print server.printName()
        print server.multiplyHandler(a, b)
        print server.lastMultipliedHandler()
        print " "


## OPTION 4

#
# def get_server():
#     try:
#         return next(get_server.s)
#     except StopIteration:
#         get_server.s = iter(SERVERS)
#         return next(get_server.s)
# setattr(get_server, 's', iter(SERVERS))


"""
Your code in this function
No Inputs
Output: Return the server name
"""

## Testing the function

if __name__ == '__main__':
    for i in range(9):  #range(server_range):
        print str(get_server())

## APP1
## APP2
## APP3
## APP1
## APP2
## APP3