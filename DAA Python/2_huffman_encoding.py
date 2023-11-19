import heapq

class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq 
        self.symbol=symbol 
        self.left=left 
        self.right=right 
        

    def __lt__(self,other): 
        return self.freq<other.freq

def printnodes(pnode,code):
    if pnode.symbol != '$':
        print(pnode.symbol + " : " + code)
        return
    printnodes(pnode.left,code+'0')
    printnodes(pnode.right,code+'1')

if __name__=="__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [ 5, 9, 12, 13, 16, 45]
    nodes=[]    

    for i in range(0,6): 
        heapq.heappush(nodes, node(freq[i],chars[i]))

    while len(nodes)>1:
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)
        newnode = node(left.freq+right.freq,'$',left,right)
        heapq.heappush(nodes, newnode)

    printnodes(nodes[0],'') 


