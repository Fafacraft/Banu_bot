# Liste chaînée


class Node:
  def __init__(self, data:dict, next_node = None):
    self.data = data
    self.next_node = next_node


class chained_list:
  def __init__(self, first_node:Node = None):
    self.first_node = first_node

  def append(self, data):
    if self.first_node == None:
      self.first_node = Node(data)
      return

    current_node = self.first_node
    while current_node.next_node != None: # on parcourt la liste tant qu'il y a un Node suivant
      current_node = current_node.next_node
    # lorsque le suivant est vide, on est à la fin, on ajoute
    current_node.next_node = Node(data)


  def length(self):
    if self.first_node == None:
      return 0

    current_node = self.first_node
    cpt = 1
    while current_node.next_node != None:
      current_node = current_node.next_node
      cpt += 1
    return cpt


  def get(self, i):
    if self.first_node == None:
      print("Error : Index out of range")
      return

    cpt = 0
    current_node = self.first_node
    while cpt < i:
      if current_node.next_node == None:
        print("Error : Index out of range")
        return
      current_node = current_node.next_node
      cpt = cpt+1
    return current_node.data


  def search(self, value):
    if self.first_node == None:
      return False

    current_node = self.first_node
    while current_node.data != value:
      if current_node.next_node == None:
        return False
      current_node = current_node.next_node
    return True

  def last_value(self):
    return self.get(self.length()-1)

  def clean(self):
    self.first_node = None

  def show(self):
    if self.first_node == None:
      return

    current_node = self.first_node
    print(self.first_node.data)
    while current_node.next_node != None:
      current_node = current_node.next_node
      print(current_node.data)

  def insert(self, i, value):
    if self.first_node == None:
      print("Error : Index out of range")
      return
    if i == 0:
      new_node = Node(value)
      new_node.next_node = self.first_node
      self.first_node = new_node
      return

    current_node = self.first_node
    cpt = 1
    while cpt < i:
      if current_node.next_node == None:
        print("Error : Index out of range")
        return
      current_node = current_node.next_node
      cpt += 1
    new_node = Node(value)
    new_node.next_node = current_node.next_node
    current_node.next_node = new_node
