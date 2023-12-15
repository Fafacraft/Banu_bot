# binary_tree
class Node_tree:
  def __init__(self, data):
    self.data = data
    self.true_node = None
    self.false_node = None

  def add_message(self, message, direction, old_message):
    if self.data == old_message:
      if direction:
        self.true_node = Node_tree(message)
      else :
        self.false_node = Node_tree(message)
    else:
      if self.true_node != None:
        self.true_node.add_message(message, direction, old_message)
      if self.false_node != None:
        self.false_node.add_message(message, direction, old_message)

  def isALeaf(self):
    if self.true_node == None and self.false_node == None:
      return True
    else:
      return False



class Discusion_tree:
  def __init__(self, root_data):
    self.root = Node_tree(root_data)
    self.current_node = self.root

  def next_node(self, direction):
    if direction:
      if self.current_node.true_node != None:
        self.current_node = self.current_node.true_node
    else:
      if self.current_node.false_node != None:
        self.current_node = self.current_node.false_node

  def get_current(self):
    return self.current_node.data

  def add_message(self, message, direction, old_message):
    self.root.add_message(message, direction, old_message)

  def reset(self):
    self.current_node = self.root

  # return if current_node is a leaf, with no childs
  def isAtLeaf(self):
    return self.current_node.isALeaf()
    
  # only work for our ship discussion Tree. Should probably start with node = self.root, as it is the subtree where it will search.
  def isThereShip(self, childShip, node):
    # if is a leaf, one of two thing ; it is the right data, or it is not
    if (node.isALeaf()):
      if node.data[0] == childShip:
        return True
      else:
        return False
    # else check all 4 cases ; both childs are None, one of them is None, or both are not None - and recursively ask if there is the ship in these subtrees
    else:
      if node.true_node == None:
        if node.false_node == None:
          print("Discussion_tree.isThereShip : Should've not been here")
          return False  # useless as it would be a leaf and should be already handled, but anyway, it makes more sense
        else:
          return self.isThereShip(childShip, node.false_node)
      else:
        if node.false_node == None:
          return self.isThereShip(childShip, node.true_node)
        else:
          return self.isThereShip(childShip, node.true_node) or self.isThereShip(childShip, node.false_node)  # if u find it in one of them it's good

        