class BFSOnMatrix:

    def __init__(self):
        self.matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        self.visited = []
        self.m = 3
        self.n = 4
    def isValid(self,x,y):
        return 0 <= x < self.m and 0 <= y < self.n
    def BFS(self):
        queue = []
        queue.append([0,0])
        self.visited.append([0,0])
        while queue:
            indices = queue.pop(0)
            x = indices[0]
            y = indices[1]
            print(self.matrix[x][y])
            l1 = [x+1,y]
            l2 = [x,y-1]
            l3 = [x,y+1]
            l4 = [x-1,y]
            for entry in [l1,l2,l3,l4]:
                if entry not in self.visited and self.isValid(entry[0],entry[1]):
                    queue.append(entry)
                    #print(entry)
                    self.visited.append(entry)
            # for i in [-1,1]:
            #     for j in [-1,1]:
            #         if self.isValid(x+i,x+j) and [x+i,x+j] not in self.visited:
            #             queue.append([x+i,x+j])
            #             print([x+i,x+j])
            #             self.visited.append([x+i,x+j])
example = BFSOnMatrix()
example.BFS()