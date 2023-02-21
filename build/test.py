import json
class TreeNode:
    def __init__(self,name):
        self.name = name
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

def tree_to_dict(root):
    if not root:
        return None
    node_dict = {}
    node_dict["name"] = root.name
    node_dict["children"] = [tree_to_dict(child) for child in root.children]
    return node_dict



def run():
    root = TreeNode('Eletronics')
    laptop = TreeNode('Laptop')
    root.add_child(laptop)
    mac = TreeNode('Mac')
    laptop.add_child(mac)
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Linux'))
    iphone = TreeNode('iphone')
    mac.add_child(iphone)
    tv = TreeNode('TV')
    root.add_child(tv)
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Apple'))

    root.print_tree()
    
    print(tree_to_dict(root))
        
    
    #return root
if __name__ == '__main__':
    run()
    pass
