class Node:
    parent: "Node|None"
    left: "Node|None"
    right: "Node|None"
    value: int
    

    def __init__(self, parent:"Node|None", value:int):
        self.parent = parent
        self.left = self.right = None
        self.value = value

class BST:
    __root : "Node|None"

    def __init__(self):
        self.__root = None
    
    def is_empty(self) -> bool:
        return self.__root is None
    
    def __put(self, value:int, current:"Node|None") -> None:
        if current.value == value:
            raise ValueError("Duplicate values")
        elif value < current.value:
            if current.left is None:
                current.left = Node(current,value)
            else:
                self.__put(value,current.left)
        elif value > current.value:
            if current.right is None:
                current.right = Node(current,value)
            else:
                self.__put(value,current.right)

    def put(self, value:int) -> None:
        if self.is_empty():
            self.__root = Node(None,value)
        else:
            self.__put(value, self.__root)
    
    def put2(self, value:int) -> None:
        if self.is_empty():
            self.__root = Node(None,value)
            return        
        current = self.__root
        while True:
            if current.value == value:
                raise ValueError("Duplicate values")
            elif value < current.value:
                if current.left is None:
                    current.left = Node(current,value)
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(current,value)
                    return
                else:
                    current = current.right
        
    def has(self, value:int) -> bool:
        current = self.__root
        while current is not None:
            if current.value == value: return True
            elif value < current.value: current = current.left
            elif value > current.value: current = current.right
        return False

    def min(self) -> int:
        if self.is_empty(): raise ValueError("No element in BST")
        current = self.__root
        while current.left is not None: 
            current = current.left
        return current.value

    def max(self) -> int:
        if self.is_empty(): raise ValueError("No element in BST")
        current = self.__root
        while current.right is not None: 
            current = current.right
        return current.value

    def __preorder(self, node:"Node|None"):
        if node is None: return
        print(node.value)
        self.__preorder(node.left)
        self.__preorder(node.right)

    def print_preorder(self) -> None:
        self.__preorder(self.__root)
    
    def __postorder(self, node:"Node|None"):
        if node is None: return
        self.__postorder(node.left)
        self.__postorder(node.right)
        print(node.value)

    def print_postorder(self) -> None:
        self.__postorder(self.__root)

    def __inorder(self, node:"Node|None"):
        if node is None: return
        self.__inorder(node.left)
        print(node.value)
        self.__inorder(node.right)

    def print_inorder(self) -> None:
        self.__inorder(self.__root)

    
    def __traverse(self, node:"Node|None", elements:list[int], way:str):
        if node is None: return
        if way=="pre": elements.append(node.value)
        self.__traverse(node.left, elements, way)
        if way=="in": elements.append(node.value)
        self.__traverse(node.right, elements, way)
        if way=="post": elements.append(node.value)

    def preorder(self) -> list[int]:
        elements = []
        self.__traverse(self.__root, elements,"pre")
        return elements

    def postorder(self) -> list[int]:
        elements = []
        self.__traverse(self.__root, elements, "post")
        return elements

    def inorder(self) -> list[int]:
        elements = []
        self.__traverse(self.__root, elements, "in")
        return elements


if __name__ == "__main__":
    bst = BST()
    bst.put2(20)
    bst.put(50)
    bst.put(30)
    bst.put2(3)
    bst.put(10)
    bst.put2(40)
    bst.print_inorder()
    print(bst.inorder())