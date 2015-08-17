"""Data Structures
Working with Graphs/Networks"""

import math

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 
  


# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 



	

left_side1=[]
left_side2=[]
right_side=[]
left_side1=[16, 32,48,64,80, 96, 112, 128,144,160,176,192, 208, 224]
#left_side2=[32,64,96,128,160,192,224]
right_side1=[15,31,47,63,79,95,111, 127,143, 159, 175, 191, 207, 223, 239]
#right_side2=[47,79,111,143,175,207,239]

def class_net(G, nodes):
	msn=int(math.sqrt(nodes))
	msnm=int(math.sqrt(nodes)-1)
	msnp=int(math.sqrt(nodes)+1)
	for i in range(nodes):
		if i==0:
			makeLink(G, i, (i+1))
			makeLink(G, i, (i+msn))
		elif i==(math.sqrt(nodes)-1):
			makeLink(G, i, (i-1))
			makeLink(G, i, (i+msn))
		elif i==(nodes-1):
			makeLink(G, i, (i-1))
			makeLink(G, i, (i-msn))
		elif i==((nodes-1)-(msn-1)):
			makeLink(G, i, (i+1))
			makeLink(G, i, (i-msn))	
		elif i in range(1,msn-1):
			makeLink(G, i, (i+1))
		elif i in range(nodes-msn+1,nodes-1):
			makeLink(G, i, (i+1))
		elif i in left_side1:
			makeLink(G, i, (i+msn))
		elif i in right_side1:
			makeLink(G, i, (i+msn))		
		else:
			makeLink(G, i, (i+1))
			makeLink(G, i, (i-1))
			makeLink(G, i, (i+msn))
			makeLink(G, i, (i-msn))
	print left_side1
	print right_side1
			
			
			

# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
####Making square graph
class Node():
	def __init__(self,value=None):
		self.value=value
		self.parent=None
		self.children=[None,None]			
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.children !=(None,None):
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.children[0],self.children[1])
		else: return "Node value: %s" %self.value

# TODO: define a function countEdges


def countEdges(G):
	edges=sum([len(G[node]) for node in G.keys()])/2 
	print edges
	
#257	

import networkx as nx
import matplotlib.pyplot as plt
def draw_graph(graph):
	# extract nodes from graph
	nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
	# create networkx graph
	G=nx.Graph()
	# add nodes
	for node in nodes:
		G.add_node(node)
	# add edges
	for edge in graph:
		G.add_edge(edge[0], edge[1])
	# draw graph
	pos = nx.shell_layout(G)
	nx.draw(G, pos)
	# show graph
	plt.show()

# Social Network
class Actor(object):
	def __init__(self, name):
		self.name = name 

  	def __repr__(self):
		return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
7
# How many edges in movies?
10
def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [] 
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
