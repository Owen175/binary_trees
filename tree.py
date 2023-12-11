# Binary trees
import random
class Tree:
    def __init__(self, tree=None):
        if tree:
            self.tree = tree
        else:
            self.tree = {}
            
    def __str__(self):
        return str(self.tree)
    
    def force_add_data(self, nodeName, right=None, parent=None, root=False):

        if not parent:
            print('Error - no inheritor and no root')
            return -1
        if parent:
            print('Error - inheritor and root')
            return -1
        if parent:
            if right:
                update = (self.tree[parent][0], nodeName)
            else:
                update = (nodeName, self.tree[inheritor][1])
            self.tree[parent] = update
        self.tree[nodeName] = (None, None)
        
    def add_datapoint(self, value: int):
        placed = False
        keys = list(self.tree.keys())
        if len(keys) == 0:
            self.tree[value] = (None, None)
            return self.tree
        node = keys[0]
        while not placed:
            if value > node:
                if self.tree[node][1] == None:
                    self.tree[node] = (self.tree[node][0], value)
                    self.tree[value] = (None, None)
                    placed=True
                if not placed:
                    node = self.tree[node][1]
            elif value < node and not placed:
                if self.tree[node][0] == None:
                    self.tree[node] = (value, self.tree[node][1])
                    self.tree[value] = (None, None)
                    placed=True
                if not placed:
                    node = self.tree[node][0]
                
                
    def inOrderTraverse(self, node=None):
        if node is None:
            node = list(self.tree.keys())[0]
        if self.tree[node][0] is not None:
            self.inOrderTraverse(self.tree[node][0])
        print(node)
        if self.tree[node][1] is not None:
            self.inOrderTraverse(self.tree[node][1])

    def preOrderTraverse(self, node=None):
        if node is None:
            node = list(self.tree.keys())[0]
        print(node)
        if self.tree[node][0] is not None:
            self.preOrderTraverse(self.tree[node][0])
        if self.tree[node][1] is not None:
            self.preOrderTraverse(self.tree[node][1])
            
    def postOrderTraverse(self, node=None):
        if node is None:
            node = list(self.tree.keys())[0]
        if self.tree[node][0] is not None:
            self.postOrderTraverse(self.tree[node][0])
        if self.tree[node][1] is not None:
            self.postOrderTraverse(self.tree[node][1])
        print(node)

if __name__ == '__main__':
    rg = list(range(0,100))
    random.shuffle(rg)
    tree=Tree()
    for r in rg:
        tree.add_datapoint(r)
    print(tree)
    tree.inOrderTraverse()
