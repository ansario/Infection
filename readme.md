README:

This program simulates an infection of several randomly generated nodes. The nodes are part of a directed graph. All nodes without parent nodes are infected by default. A breadth-first search algorithm is employed to traverse the nodes and infect them. Nodes which are green are non-infected and nodes which are red are infected. A print out of each step can be viewed in the same direcotry as the directory from which the program was executed.

This program utilizes the networkx module in Python available from https://networkx.github.io. It also uses matplotlib available from http://matplotlib.org.

You can obtain these modules by using pip. Run the following commands:

sudo pip-install networkx
sudo pip-install matplotlib

Problems:

There sometimes can be a problem with the limited infection algorithm. The algorithm works by removing 4 nodes from the list of available nodes to infect. This can work to prevent all the nodes from being infected. Sometimes it does not work if all the nodes have several paths leading to all of them. This could be corrected with more time to implement a more effecient algorithm.

Future additions:

I would like to add a timing function to determine the length of time it takes to infect all the nodes on the graph.