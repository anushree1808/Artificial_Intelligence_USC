import collections

class homework1:

    def __init__(self):
        self.start=""
        self.goal = ""
        self.no_of_lines = ""
        self.no_of_states = ""
        self.algo = ""
        self.live_data = []
        self.sunday_traffic = dict()
        self.sec_n = dict() # serves as a backtracking data structure (stores every node once , more like explored nodes)
        self.graph = collections.defaultdict(list) # creating dictionary of lists for adjacency list representation

    def bfs(self):
        nodes = collections.deque()
        
        #create start node
        start_node = {'state' : self.start, 'pathcost' : 0, 'parent' : None}
        
        #enqueue start node
        nodes.appendleft(start_node) #the actual nodes queue
        self.sec_n[self.start] = start_node 

        #set required variables
        condition = True
        cur_state = self.start

        #bfs logic
        while condition:
            if len(nodes) == 0:
                break

            node = nodes.pop()
            # Goal Test
            if node['state'] == self.goal:
                break

            # Queueing fn
            else:
                #cost = cost+1
                cur_state = node['state']
                par_node = node
                i=0

                # Check for all the child nodes to expand the current node and also ignore the nodes that are already visited.
                for child in self.graph[cur_state]:
                    st = child[0]
                    if st not in self.sec_n:
                        node = {'state':st,'pathcost':par_node['pathcost']+1, 'parent':cur_state }
                        nodes.appendleft(node)
                        self.sec_n[st] = node
                
            #prev_state = cur_state
        
        if node['state'] == self.goal:
            return self.BuildResult(node)
        elif len(nodes) == 0:
            return None
        else :
            return None

    def dfs(self):
        #print "dfs"
        nodes_open = collections.deque()
        n_open = dict()
        nodes_closed = collections.deque()
        n_closed = dict()
        
        #create start node
        start_node = {'state' : self.start, 'pathcost' : 0, 'parent' : None}

        #enqueue start node
        nodes_open.appendleft(start_node) #the actual nodes queue
        n_open[self.start] = start_node

        condition = True

        while condition :
            if len(nodes_open) == 0:
                break

            cur_node = nodes_open.popleft()
            n_open.pop(cur_node['state'],None)
            
            nodes_closed.appendleft(cur_node)
            n_closed[cur_node['state']] = cur_node
            
            if cur_node['state'] == self.goal:
                break

            child_nodes = self.graph[cur_node['state']] # returns child nodes and the distances from cur_node to them
            #print child_nodes
            i = len(child_nodes)-1
            while i >= 0 :
                child = child_nodes[i]
                i = i-1

                if child[0] in n_open:
                    if 1+cur_node['pathcost'] < n_open[child[0]]['pathcost']:
                        nodes_open.remove(n_open[child[0]])
                        n_open.pop(child[0], None)
                        node = {'state':child[0],'pathcost': 1+cur_node['pathcost'],'parent':cur_node['state']}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] in n_closed:
                    if 1+cur_node['pathcost'] < n_closed[child[0]]['pathcost']:
                        nodes_closed.remove(n_open[child[0]])
                        n_closed.pop(child[0], None)
                        node = {'state':child[0],'pathcost': 1+cur_node['pathcost'],'parent':cur_node['state']}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] not in n_closed or child[0] not in n_open:
                    node = {'state':child[0],'pathcost': 1+cur_node['pathcost'],'parent':cur_node['state']}
                    nodes_open.appendleft(node)
                    n_open[child[0]] = node

            

        #print nodes_open
        #print n_closed
            
        if cur_node['state'] == self.goal:
            self.sec_n = n_closed
            self.sec_n [cur_node['state']] = cur_node
            return self.BuildResult(cur_node)
        
        elif len(nodes_open) == 0:
            #print 0
            return None
        
        else :
            return None

    def ucs(self):
        nodes_open = collections.deque()
        n_open = dict()
        nodes_closed = collections.deque()
        n_closed = dict()
        
        #create start node
        start_node = {'state' : self.start, 'pathcost' : 0, 'parent' : None}

        #enqueue start node
        nodes_open.appendleft(start_node) #the actual nodes queue
        n_open[self.start] = start_node

        nodes_closed.appendleft(start_node)
        n_closed[start_node['state']] = start_node

        condition = True

        while condition :
            if len(nodes_open) == 0:
                break

            cur_node = nodes_open.pop()
            n_open.pop(cur_node['state'],None)
            nodes_closed.appendleft(cur_node)
            n_closed[cur_node['state']] = cur_node
            
            if cur_node['state'] == self.goal:
                break

            child_nodes = self.graph[cur_node['state']] # returns child nodes and the distances from cur_node to them
            i = 0
            while len(child_nodes)>i :
                child = child_nodes[i]
                i = i+1

                if child[0] in n_open:
                    if child[1]+cur_node['pathcost'] < n_open[child[0]]['pathcost']:
                        nodes_open.remove(n_open[child[0]])
                        n_open.pop(child[0], None)
                        node = {'state':child[0],'pathcost': child[1]+cur_node['pathcost'],'parent':cur_node['state']}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] in n_closed:
                    if child[1]+cur_node['pathcost'] < n_closed[child[0]]['pathcost']:
                        nodes_closed.remove(n_open[child[0]])
                        n_closed.pop(child[0], None)
                        node = {'state':child[0],'pathcost': child[1]+cur_node['pathcost'],'parent':cur_node['state']}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] not in n_closed or child[0] not in n_open:
                    node = {'state':child[0],'pathcost': child[1]+cur_node['pathcost'],'parent':cur_node['state']}
                    nodes_open.appendleft(node)
                    n_open[child[0]] = node

            nodes_open = sorted(nodes_open, key=lambda k: k['pathcost'], reverse=True)
            nodes_open = collections.deque(nodes_open)
        #print n_open
        #print n_closed
            
        if cur_node['state'] == self.goal:
            self.sec_n = n_closed
            self.sec_n [cur_node['state']] = cur_node
            return self.BuildResult(cur_node)
        
        elif len(nodes_open) == 0:
            #print 0
            return None
        
        else :
            #print 4
            return None
        
        
    def a_star(self):
        #print "a*"
        nodes_open = collections.deque()
        n_open = dict()
        nodes_closed = collections.deque()
        n_closed = dict()
        
        #create start node
        start_node = {'state' : self.start, 'pathcost' : 0, 'parent' : None, 'h_n' :self.sunday_traffic[self.start] } #g(n)=pathcost ; f_n = h_n + g(n)
        start_node['f_n'] = start_node['h_n']+start_node['pathcost']

        #enqueue start node
        nodes_open.appendleft(start_node) #the actual nodes queue
        n_open[self.start] = start_node

        condition = True

        while condition :
            if len(nodes_open) == 0:
                break

            #print nodes_open
            cur_node = nodes_open.pop()
            n_open.pop(cur_node['state'],None)
            nodes_closed.appendleft(cur_node)
            n_closed[cur_node['state']] = cur_node
            
            if cur_node['state'] == self.goal:
                break

            child_nodes = self.graph[cur_node['state']] # returns child nodes and the distances from cur_node to them
            #print child_nodes
            i = 0
            while len(child_nodes)>i :
                child = child_nodes[i]
                i = i+1
                pathcost =  child[1]+cur_node['pathcost']
                h_n = self.sunday_traffic[child[0]]
                f_n = pathcost+h_n
                #print f_n
                if child[0] in n_open:
                    #print child[0]
                    if f_n< n_open[child[0]]['f_n']:
                        #print child[0]
                        nodes_open.remove(n_open[child[0]])
                        n_open.pop(child[0],None)
                        node = {'state':child[0],'pathcost':pathcost,'parent':cur_node['state'],'h_n':h_n,'f_n':f_n}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] in n_closed:
                    if f_n < n_closed[child[0]]['f_n']:
                        #print child[0]
                        nodes_closed.remove(n_closed[child[0]])
                        n_closed.pop(child[0],None)
                        node = {'state':child[0],'pathcost':pathcost,'parent':cur_node['state'],'h_n':h_n,'f_n':f_n}
                        nodes_open.appendleft(node)
                        n_open[child[0]] = node

                elif child[0] not in n_closed or child[0] not in n_open:
                    node = {'state':child[0],'pathcost':pathcost,'parent':cur_node['state'],'h_n':h_n,'f_n':f_n}
                    nodes_open.appendleft(node)
                    n_open[child[0]] = node

            nodes_open = sorted(nodes_open, key=lambda k: k['f_n'], reverse=True)
            nodes_open = collections.deque(nodes_open)

            #print n_open
            #print nodes_open
            #print "\n\n"
        #print n_open
        #print n_closed
            
        if cur_node['state'] == self.goal:
            self.sec_n = n_closed
            self.sec_n [cur_node['state']] = cur_node
            return self.BuildResult(cur_node)
        
        elif len(nodes_open) == 0:
            return None
        
        else :
            return None


    def ReadInput(self, fname):
        fo = open(fname,'rU')
        content = []
        with fo as f:
            self.content = [line.strip() for line in f.readlines()]

        self.algo = self.content[0]
        self.start = self.content[1]
        self.goal = self.content[2]
        self.no_of_lines = int(self.content[3])

        for i in range(self.no_of_lines):
            det = self.content[4+i].split(" ")
            self.live_data.append([det[0], det[1], int(det[2])])

        temp1 = 4+self.no_of_lines
        self.no_of_states = int(self.content[temp1])
        temp2 = temp1+1

        for i in range(self.no_of_states):
            det = self.content[temp2+i].split(" ")
            self.sunday_traffic[det[0]] = int(det[1])

        self.BuildGraph()
        fo.close()
        return self.algo

    def WriteOutput(self, res):
        fname = "output.txt"
        fo = open(fname, 'w')
        outlist = []
        while len(res)>0:
            st = res[0]['state']+" "+str(res[0]['pathcost'])+"\n"
            outlist.append(st)
            res.popleft()
        print outlist
        fo.writelines(outlist)
        fo.close()

    def BuildGraph(self):
        for data in self.live_data:
            self.graph[data[0]].append([data[1],data[2]])
        #print self.graph['1']

    def BuildResult(self, node):
        #print self.sec_n
        result = collections.deque()
        result.appendleft(node)
        while (node['state'] != self.start):
            node = self.sec_n[node['parent']]
            result.appendleft(node)
        #print result
        return result
            
obj = homework1()
algo = obj.ReadInput("input/input3.txt")
print algo
if algo == "BFS" :
    res = obj.bfs()
    if res :
        obj.WriteOutput(res)
elif algo == "DFS":
    res = obj.dfs()
    if res :
        obj.WriteOutput(res)
elif algo == "UCS":
    res = obj.ucs()
    if res :
        obj.WriteOutput(res)
elif algo == "A*":
    res = obj.a_star()
    if res :
        obj.WriteOutput(res)
else :
    exit
    
#print obj.live_data
#print obj.sunday_traffic
