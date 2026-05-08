import math
#from typing import Generic, TypeVar

#T = TypeVar("T")


########################################################################


def get_integer():

    while True:
        try:
            print("Please enter an integer and this program will tell you if it is prime!")
            return int(input())

        except ValueError:
            print("That was not a number... Try again...")

def check_prime(possible_prime):

    if possible_prime <= 1:
        print(f'{possible_prime} is not prime')

    else:
        for i in range(2,int(math.sqrt(possible_prime)) + 1): #int() is implicitly a floor function
            if possible_prime % i == 0:
                print(f'{possible_prime} is not prime')
                break

        else:
            print(f'{possible_prime} is prime')


class TreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data) #self.root type: TreeNode | None, but we check for None, so it's fine

    def _insert(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = TreeNode(data)
            else:
                self._insert(root.right, data)

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)
        print(root.data, end=", ")
        self.in_order(root.right)


def main():
    check_prime(get_integer())

    tree = BST()

    for i in range(0,10):
        tree.add_node(i)

    tree.in_order(tree.root)




if __name__ == '__main__':
    main()
