class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")

    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next

def insert_node(data):
    global node_A
    new_node = Node(data)
    if node_A.data > new_node.data:
        new_node.next = node_A
    else:
        pre_node = node_A
        next_node = node_A.next
        while next_node:
            if next_node.data> new_node.data:
                print(new_node.data + "삽입!")
                pre_node.next = new_node
                new_node.next = next_node
                break
            else:
                pre_node = pre_node.next
                next_node = pre_node.next

def delete_node(data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if node_A.data == data:
        node_A = next_node
        del pre_node
    else:
        while next_node:
            if next_node.data == data:
                print(next_node.data + "제거!")
                pre_node.next = next_node.next
                del next_node
                break
            pre_node = next_node
            next_node = next_node.next

if __name__=="__main__":
    init_list()
    insert_node("C")
    print_list()
    delete_node("C")
    print_list()
