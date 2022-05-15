from typing import List


class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return str(self.value)


class NodeTree:
    def __init__(self, nodes: List[List[Node]]):
        self.nodes = nodes

    def find_max_path_sum(self):
        nodes_to_search = self.nodes
        if len(self.nodes[0]) == 1:
            nodes_to_search = list(reversed(self.nodes))

        for node_line in nodes_to_search:
            for node in node_line:
                left_value = 0 if node.left is None else node.left.value
                right_value = 0 if node.right is None else node.right.value
                node.value = node.value + max(left_value, right_value)

        return nodes_to_search[len(nodes_to_search) - 1][0].value

    @staticmethod
    def create_node_tree_from_str(node_tree: str) -> 'NodeTree':
        line_index = 0
        child_index = 0

        nodes: List[List[Node]] = [[]]

        for line in node_tree.split('\n'):
            for string_number in line.lstrip().rstrip().split(' '):
                if len(nodes) < (line_index + 1):
                    nodes.append([])
                node = Node(int(string_number))
                nodes[line_index].append(node)

                if line_index > 0:
                    previous_line = nodes[line_index - 1]

                    if len(previous_line) > child_index:
                        previous_line[child_index].left = node

                    if child_index > 0:
                        previous_line[child_index - 1].right = node
                child_index += 1
            child_index = 0
            line_index += 1

        return NodeTree(nodes)
