from typing import List
import hashlib


class Node:
    def __init__(self, left, right, value: str, content) -> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.content = content

    @staticmethod
    def hash(val: str) -> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def __str__(self):
        return str(self.value)


class MerkleTreeExample:
    def __init__(self, values: List[str]) -> None:
        self.__build_tree(values)

    def __build_tree(self, values: List[str]) -> None:

        leaves: List[Node] = [Node(None, None, Node.hash(e), e) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0])  # duplicate last elem if odd number of elements
            self.root: Node = self.__build_tree_rec(leaves)

    def __build_tree_rec(self, nodes: List[Node]) -> Node:
        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value),
                        nodes[0].content + "+" + nodes[1].content)
        left: Node = self.__build_tree_rec(nodes[:half])
        right: Node = self.__build_tree_rec(nodes[half:])
        value: str = Node.hash(left.value + right.value)
        content: str = self.__build_tree_rec(nodes[:half]).content + "+" + self.__build_tree_rec(nodes[half:]).content
        return Node(left, right, value, content)

    def print_tree(self) -> None:
        self.__print_tree_rec(self.root)

    def __print_tree_rec(self, node) -> None:
        if node is not None:
            if node.left is not None:
                print("Left: " + str(node.left))
                print("Right: " + str(node.right))
            else:
                print("Input")

            print("Value: " + str(node.value))
            print("Content: " + str(node.content))
            print("")
            self.__print_tree_rec(node.left)
            self.__print_tree_rec(node.right)

    def get_root_hash(self) -> str:
        return self.root.value


def mix_merkle_tree() -> None:
    elems = ["Hello", "World", "Merkle", "Tree", "Anton", "Aks", "GO"]
    print("Inputs: ")
    print(*elems, sep=" | ")
    print("")
    mtree = MerkleTreeExample(elems)
    print("Root Hash: " + mtree.get_root_hash() + "\n")
    print(mtree.print_tree())


if __name__ == '__main__':
    mix_merkle_tree()
