import json
class TreeNode:

    def __init__(self,name,id,level):
        self.name = name
        self.id = id
        self.level = level
        self.children = []
        self. parent = None
    def add_child(self,child):
        self.child = child 
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0 
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level 
    def print_tree(self):
        print('  '*self.get_level() + '|--', end = '')
        print(self.name)
        if self.children:
            for each in self.children:
                each.print_tree()

def BFS(root):
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        for i in temp.children:
            queue.append(i)
        print(temp.name)

def DFS(root):
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop()
        for i in temp.children:
            queue.append(i)
        print(temp.name)

def NodeOfLevel(root,level):
    lst = []
    queue = [root]
    while queue:
        temp = queue.pop(0)
        for i in temp.children:
            queue.append(i)
        if temp.level == level:
            lst.append(temp)
    return lst


def tree_to_dict(root):
    if not root:
        return None
    node_dict = {}
    node_dict["name"] = root.name
    node_dict["children"] = [tree_to_dict(child) for child in root.children]
    return node_dict

