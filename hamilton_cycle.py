"""Q.Program to implement Hamilton Cycle using Backtracking"""

class Hamiltonian:
  def __init__(self, start):
    self.start = start            #start (& end) vertex 
    self.cycle = []               #list to store the cycle path
    self.hasCycle = False         #varibale to mark if graph has the cycle

  def findCycle(self):            #method to inititate the search of cycle
    self.cycle.append(self.start) #add starting vertex to the list
    self.solve(self.start)        #start the search of the hamiltonian cycle  
  
  def solve(self, vertex):        #recursive function to implement backtracking
    #Base condition: if the vertex is the start vertex
    #and all nodes have been visited (start vertex twice)
    if vertex == self.start and len(self.cycle) == N+1:
      self.hasCycle = True 
      self.displayCycle()         #output the cycle 
      return                      #return to explore more cycles

    for i in range(len(vertices)):#iterate through the neighbor vertices
      if adjacencyM[vertex][i] == 1 and visited[i] == 0:
        nbr = i
        visited[nbr] = 1          #visit and add vertex to the cycle
        self.cycle.append(nbr)
        self.solve(nbr)           #traverse the neighbor vertex to find the cycle
        visited[nbr] = 0          #Backtrack
        self.cycle.pop()

  def displayCycle(self):         #function to display the hamiltonian class
    names = []
    for v in self.cycle:
      names.append(vertices[v])
    print(names)
    
if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D']
    adjacencyM = [[0, 1, 0, 1],
                  [1, 0, 1, 0],
                  [0, 1, 0, 1],
                  [1, 0, 1, 0],]

    visited = [0 for x in range(len(vertices))]  #list mapping of vertices to mark vertex visited
    N = 4                                     #number of vertices in the graph
  
    #Driver code
    hamiltonian = Hamiltonian(0)
    hamiltonian.findCycle()
    if not hamiltonian.hasCycle:                 #if the graph doesn't have any Hamiltonian Cycle
        print("No Hamiltonian Cycle")