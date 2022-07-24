'''
    The "Node" structure will hold a pointer to
    the next node and a some data (value).

    Below is a visual of a new node for reference.
'''


##########################
#
#     Node
#   ---------
#   | Value |
#   | ----- |
#   | Next  |----> None
#   ---------
#
##########################
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


'''
    The LinkedList class starts off with a new node, head, and tail upon object creation.
'''


class LinkedList:
    def __init__(self, value):

        new_node = Node(value)

        # Create a head of type Node
        self.head_of_linkedlist = new_node

        # Create a tail of type Node
        self.tail_of_linkedlist = new_node

        # Print head and tail node ascii art
        self.print_head_tail_ascii_art(value)
        self.length = 0

    def append_new_node_to_linked_list(self, value):
        # Create a new node and add data/value

        ##########################
        #
        #     Node
        #   ---------
        #   | Value |
        #   | ----- |
        #   | Next  |----> None
        #   ---------
        #
        ##########################
        new_node = Node(value)

        # Head and tail start out pointing to None until a node is added.

        ##########################
        #
        #     Head
        #   ---------
        #   | Value |
        #   | ----- |
        #   | Next  |----> None
        #   ---------
        #
        #     Tail
        #   ---------
        #   | Value |
        #   | ----- |
        #   | Next  |----> None
        #   ---------
        #
        ##########################

        # If the pointer to the first node is None i.e. a node hasn't been added to the linked list,
        # then point the head and tail to the first node created.
        if self.head_of_linkedlist.next_node is None:

            # Point head and tail to new node

            ##########################
            #
            #     Head
            #   ---------
            #   | Value |
            #   | ----- |
            #   | Next  |\                 New Node
            #   --------- \               ---------
            #              \              | Value |
            #     Tail      ------------> | ----- |
            #   ---------   /             | Next  |----> None
            #   | Value |  /              ---------
            #   | ----- | /
            #   | Next  |/
            #   ---------
            #
            ##########################

            # Point the head to the first node's address.
            self.head_of_linkedlist.next_node = new_node
            self.head_of_linkedlist.value = new_node.value

            # Point the tail to the first node's address.
            self.tail_of_linkedlist.next_node = new_node
            self.tail_of_linkedlist.value = new_node.value

            # Print visual
            self.print_first_node_added_to_linked_list_ascii_art(self.head_of_linkedlist.value,
                                                                 self.tail_of_linkedlist.value,
                                                                 new_node.value)

        # Else point the tail to the new node

        ##########################
        #
        #     Head
        #   ---------
        #   | Value |
        #   | ----- |
        #   | Next  |\                 Node A              Node B
        #   --------- \               ---------           ---------
        #              \              | Value |           | Value |
        #               ------------> | ----- |           | ----- |
        #                             | Next  |---------> | Next  |-----> None
        #                             ---------           ---------
        #     Tail                                       ^
        #  ----------                                   /
        #  | Value  |                                  /
        #  | ------ |                                 /
        #  | Next   |-------------------------------->
        #  ----------
        #
        ##########################
        else:
            # The tail will now point to the new node we wish to append to the linked list
            self.tail_of_linkedlist.next_node = new_node

            # Set tail's value equal to the new nodes value
            self.tail_of_linkedlist = new_node
            self.print_second_node_added_to_linked_list(self.head_of_linkedlist.value,
                                                        self.head_of_linkedlist.value,
                                                        self.tail_of_linkedlist.value, new_node.value)
        # Increase the node count by one
        self.length += 1

        return True

    def print_head_tail_ascii_art(self, val):
        display_head_and_tail_visual = f"""
        Upon the LinkedList's creation, the head and tail nodes will be constructed and point to None.

              Head
            ---------
            |   {val}   |
            | ----- |
            | Next  |----> None
            ---------
        
              Tail
            ---------
            |   {val}   |
            | ----- |
            | Next  |----> None
            ---------
        """
        return print(display_head_and_tail_visual)

    def print_first_node_added_to_linked_list_ascii_art(self, hv, tv, nv):
        art = f'''
        The head and tail will both point to the same node if only one node exists.
        
              Head
            ---------
            |   {hv}   |
            | ----- |
            | Next  |\                 New Node
            --------- \               ---------
                       \              |   {nv}   |
              Tail      ------------> | ----- |
            ---------   /             | Next  |----> None
            |   {tv}   |  /              ---------
            | ----- | /
            | Next  |/
            ---------
        '''
        return print(art)

    def print_second_node_added_to_linked_list(self, hv, hnv, tv=0, nv=0):
        art = f'''
        When the LinkedList has more than one node, the head always point to the 1st node and the tail the last node.
        
              Head
            ---------
            |   {hv}   |
            | ----- |
            | Next  |\                 Node A              Node B
            --------- \               ---------           ---------
                       \              |   {hnv}   |           |   {nv}   |
                        ------------> | ----- |           | ----- |
                                      | Next  |---------> | Next  |-----> None
                                      ---------           ---------
              Tail                                       ^
           ----------                                   /
           |   {tv}    |                                  /
           | ------ |                                 /
           | Next   |-------------------------------->
           ----------
        '''

        return print(art)

    def print_node_address(self, text, node):
        node_address = id(node)
        return print(f"{text} " + str(node_address))

    def print_list(self):
        temp = self.head_of_linkedlist
        while temp is not None:
            print(temp.value)
            temp = temp.next_node


my_linked_list = LinkedList(1)
my_linked_list.append_new_node_to_linked_list(2)
my_linked_list.append_new_node_to_linked_list(3)
