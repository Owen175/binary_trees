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
        
        node = self.getRoot()
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
                
    def getRoot(self):
        for key, value in self.tree.items():
            for k, v in self.tree.items():
                if key in v:
                    break
            else:
                return key
        
    def inOrderTraverse(self, node=None):
        if node is None:
            node = self.getRoot()
        if self.tree[node][0] is not None:
            self.inOrderTraverse(self.tree[node][0])
        print(node)
        if self.tree[node][1] is not None:
            self.inOrderTraverse(self.tree[node][1])

    def preOrderTraverse(self, node=None):
        if node is None:
            node = self.getRoot()
        print(node)
        if self.tree[node][0] is not None:
            self.preOrderTraverse(self.tree[node][0])
        if self.tree[node][1] is not None:
            self.preOrderTraverse(self.tree[node][1])
            
    def postOrderTraverse(self, node=None):
        if node is None:
            node = self.getRoot()
        if self.tree[node][0] is not None:
            self.postOrderTraverse(self.tree[node][0])
        if self.tree[node][1] is not None:
            self.postOrderTraverse(self.tree[node][1])
        print(node)
        
    def delete(self, name):
        if name not in self.tree:
            print('Error: Not in tree!')
            return
        if self.tree[name] == (None, None):
            self.tree.pop(name)
        elif self.tree[name][0] == None or self.tree[name][1] == None:
            if self.tree[name][0] == None:
                child = self.tree[name][1]
            else:
                child = self.tree[name][0]
            for key, value in self.tree.items():
                if value[0] == name:
                    self.tree[key] = (child, self.tree[key][1])
                if value[1] == name:
                    self.tree[key] = (self.tree[key][0], child)
            self.tree.pop(name)
        else:
            replacement = self.findLargestUnder(name)
            self.delete(replacement)
            for key, value in self.tree.items():
                if value[0] == name:
                    self.tree[key] = (replacement, self.tree[key][1])
                if value[1] == name:
                    self.tree[key] = (self.tree[key][0], replacement)
            self.tree[replacement] = self.tree[name]
            self.tree.pop(name)
        for key, value in self.tree.items():
            if value[0] == name:
                self.tree[key] = (None, self.tree[key][1])
            if value[1] == name:
                self.tree[key] = (self.tree[key][0], None)
                
    def findLargestUnder(self, name):
        val = self.tree[name][0]
        lastval = val
        while val is not None:
            lastval = val
            val = self.tree[val][1]
        return lastval
            
if __name__ == '__main__':
    rg = list(range(0,100))
    random.shuffle(rg)
    tree=Tree()
    for r in rg:
        tree.add_datapoint(r)
    base = tree.getRoot()
    tree.delete(base)
    tree.inOrderTraverse()


