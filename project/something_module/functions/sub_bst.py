class SubNode(object):
    """Basic Node object for use in a Binary Search Tree.

    :param data: The data enveloped by the Node.
    :type data: int
    """

    data: int = None
    l_child: "SubNode" = (
        None  #: The left child of the Node. Everything in this sub-tree should be < ``data``.
    )
    r_child: "SubNode" = (
        None  #: The right child of the Node. Everything in this sub-tree should be > ``data``.
    )

    def __init__(self, data: int):
        self.data = data

    def __repr__(self) -> str:
        return "data: {}, r_child: {}, l_child: {}".format(
            self.data, self.r_child, self.l_child
        )


class SubBinarySearchTree(object):
    """Basic BST object supporting pre-order, in-order, post-order traversal. This tree assumes that all values added through ``insert_node`` are unique."""

    root: SubNode = None

    def insert_node(self, data: int) -> None:
        """Inserts a node into the Binary Search Tree

        :param data: The number to insert into the BST.
        :type data: int
        """
        node = SubNode(data)

        if self.root is None:
            self.root = node
            return

        curr_root = self.root

        while True:
            if node.data < curr_root.data:
                if curr_root.l_child:
                    curr_root = curr_root.l_child
                    continue
                curr_root.l_child = node
                return
            else:
                if curr_root.r_child:
                    curr_root = curr_root.r_child
                    continue
                curr_root.r_child = node
                return
