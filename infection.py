###############################################################################
# Copyright (c) 2015 Omar A. Ansari
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation file (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#
# This program utilizes the networkx module to generate a random directed graph
# and attempts to traverse the nodes generated in the graph to "infect" all 
# the nodes by turning them red. An image is generated at each step and can be
# found in the same directory as this program. 
###############################################################################
###############################################################################
# MODULES
###############################################################################
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.traversal.breadth_first_search import bfs_edges
###############################################################################
# CLASS
###############################################################################
class Infection:

#########################################################################
# Method: genRandom(self)
#
# This method randomly generates a directed graph with 75 nodes and a 5%
# chance of paths being created between nodes.
# 
#########################################################################
	
	def genRandom(self):

		G = nx.gnp_random_graph(75, .05, directed = True)

		return G

#########################################################################
# Method: printGraph(self, graph, infectedNodes, count, colors, name)
#
# This method utilizes the matplotlib module in order to generate a graph
# of the nodes passed as parameter. It labels each node with its number
# and colors each node based on whether or not they are infected.
#
# Param:
#
# graph -- graph which will be printed out.
# infectedNodes -- nodes which are infected and will be colored red.
# count -- number used to indicate what position this print out is in the
# overall printouts. This is used for filenaming.
# colors -- list of colors for infected(red)/nonInfected(green) nodes.
# name -- Name of type of infection for file creation.
#
#########################################################################
	
	def printGraph(self, graph, infectedNodes, count, colors, name):

		pos = nx.circular_layout(graph)
		pos = nx.spring_layout(graph, dim = 2, pos = pos)
		for x in graph.nodes():
			graph.node[x]['value'] = x
		
		node_labels = nx.get_node_attributes(G, 'value')
		nx.draw_networkx_labels(graph, pos, labels = node_labels)

		nx.draw_networkx_nodes(graph, pos, node_color = colors, with_labels=True, font_size = 8)
		nx.draw_networkx_edges(G, pos, arrows=True)
		plt.savefig(name+str(count)+".png")
		plt.clf()

#########################################################################
# Method: colors (self, graph, infectedNodes)
#
# This method returns a list of colors for each node based on infected/
# nonInfected.
# 
# Param:
#
# graph -- graph of nodes.
# infectedNodes -- nodes which are infected and will be colored red.
#
#########################################################################
	
	def colors (self, graph, infectedNodes):
		
		colors = []

		for x in nx.nodes(graph):
			if x in infectedNodes:
				colors.append('r')
			else:
				colors.append('g')
		
		return colors

#########################################################################
# Method: getSubNodes(self, graph, node)
#
# This method returns a list of subnodes for the node passed as 
# parameter.
#
# Param:
#
# graph -- graph of nodes.
# node -- starting node to find all subnodes from.
#
#########################################################################
	
	def getSubNodes(self, graph, node):

		return graph.neighbors(node)

#########################################################################
# Method: getParentNodes(self, graph, node)
#
# This method returns a list of parent nodes for the node passed as 
# parameter.
#
# Param:
#
# graph -- graph of nodes.
# node -- starting node to find all parent nodes from.
#
#########################################################################

	def getParentNodes(self, graph, node):

		return graph.predecessors(node)

#########################################################################
# Method: infectAllNodes(self, graph, infectedNodes)
#
# Method to infect all the nodes in a graph by traversing the tree 
# utilizing a breadth-first search.
# 
# Param:
#
# graph -- graph of nodes.
# infectedNodes -- nodes which do not have any parents are infected by
# default.
#
#########################################################################
	
	def infectAllNodes(self, graph, infectedNodes):

		steps = 0
		color = []
		inNodes = infectedNodes
		
		for x in inNodes:
			try:
				
				listOfParentNodes = nx.bfs_successors(G,x).keys()
				listOfSubNodes =  nx.bfs_successors(G,x).values()
			
			except:
				continue

			print "Processing graph, please wait..."
			
			for subList in range(0, len(listOfSubNodes)):
				for item in listOfSubNodes[subList]:
					if item not in inNodes:
						inNodes.append(item)
					
				name= 'All_Infected'
				color = Infection.colors(self, graph, inNodes)
				Infection.printGraph(self, graph, inNodes, steps, color, name)
				
				steps = steps + 1

				print "Nodes infected: " + str(color.count('r'))
				print "Nodes left: " + str(len(nx.nodes(graph)))

			if color.count('r') == len(nx.nodes(graph)):
					break
	
#########################################################################
# Method: infectAllNodes(self, graph, infectedNodes)
#
# Method to infect all the nodes in a graph by traversing the tree 
# utilizing a breadth-first search. In this case, two nodes are removed
# from the beginning of the list. This essentially provides them with 
# immunity from the infection. 
# 
# Param:
#
# graph -- graph of nodes.
# infectedNodes -- nodes which do not have any parents are infected by
# default.
#
#########################################################################
	
	def limitedInfection(self, graph, infectedNodes):
		steps = 0
		color = []
		inNodes = infectedNodes

		for x in inNodes:
			try:
				
				listOfParentNodes = nx.bfs_successors(G,x).keys()
				listOfSubNodes =  nx.bfs_successors(G,x).values()
				del listOfSubNodes[0]
				del listOfSubNodes[0]
				del listOfSubNodes[0]
				del listOfSubNodes[0]
				
			except:
				continue

			print "Processing graph, please wait..."
			for subList in range(0, len(listOfSubNodes)):
				for item in listOfSubNodes[subList]:
					if item not in inNodes:
						inNodes.append(item)	
			
				name= 'Limited_Infected'
				color = Infection.colors(self, graph, inNodes)
				Infection.printGraph(self, graph, inNodes, steps, color, name)
				
				steps = steps + 1

				print "Nodes infected: " + str(color.count('r'))
				print "Nodes left: " + str(len(nx.nodes(graph)))
			
			if color.count('r') == len(nx.nodes(graph)):
					break

#########################################################################
# Method: getStartingNodes(self, graph)
#
# This method returns a list of nodes which do not have any parent nodes.
# 
# Param:
#
# graph -- graph of nodes.
#
#########################################################################
	
	def getStartingNodes(self, graph):

		nodesIterator = nx.nodes(graph)
		listOfStartingNodes = []
		
		for x in nodesIterator:
			adjacentNodes = Infection.getParentNodes(self,G, x)
			
			if not adjacentNodes:
				listOfStartingNodes.append(x)

		return listOfStartingNodes

#########################################################################
# MAIN
#########################################################################

if  __name__ =='__main__':
	
		newGraph = Infection()
		
		G = newGraph.genRandom()
		infectedNodes = newGraph.getStartingNodes(G)
 		newGraph.infectAllNodes(G, infectedNodes)
 		
 		H = newGraph.genRandom()
 		infectedNodes = newGraph.getStartingNodes(H)
 		newGraph.limitedInfection(H, infectedNodes)
 