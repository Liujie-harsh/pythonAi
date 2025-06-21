# 作者:python11-刘杰
# 2025年06月04日15时50分30秒
# xxx@qq.com
from collections import deque


class Node():
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)

    def front_scan(self, root):
        if root == None:
            return
        print(root.elem, end="")
        self.front_scan(root.left)
        self.front_scan(root.right)

    def middle_scan(self, root):
        if root == None:
            return
        self.middle_scan(root.left)
        print(root.elem, end="")
        self.middle_scan(root.right)

    def later_scan(self, root):
        if root == None:
            return
        self.later_scan(root.left)
        self.later_scan(root.right)
        print(root.elem, end="")

    def level_scan(self, root):
        if root is None:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.elem, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":
    tree = Tree()
    elems = [1, 2, 3, 4, 5, 6, 7]  # 层次建树的输入序列
    for elem in elems:
        tree.add(elem)

    print("前序遍历:", end=" ")
    tree.front_scan(tree.root)
    print("\n中序遍历:", end=" ")
    tree.middle_scan(tree.root)
    print("\n后序遍历:", end=" ")
    tree.later_scan(tree.root)
    print("\n层序遍历:", end=" ")
    tree.level_scan(tree.root)
