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



class Discusion_tree:
  def __init__(self, root = None):
    self.root = root
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