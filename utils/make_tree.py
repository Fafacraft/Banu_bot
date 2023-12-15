from custom_types.binary_tree import Discusion_tree, Node_tree

def make_tree():
    tree = Discusion_tree(["Small", "Big"])

    # layer 1
    tree.add_message(["Military", "Civil"], True, ["Small", "Big"])
    tree.add_message(["Really Big ?", "Not that much"], False, ["Small", "Big"])

    # layer 2
    tree.add_message(["Fighter", "Bomber"], True, ["Military", "Civil"])
    tree.add_message(["Versatile", "Specialized"], False, ["Military", "Civil"])

    # layer 3
    tree.add_message(["Light", "Heavy"], True, ["Fighter", "Bomber"])
    tree.add_message(["In Space", "On Land"], False, ["Fighter", "Bomber"])

    # layer 4
    tree.add_message(["Stealthy ?", "Not so much"], True, ["Light", "Heavy"])
    tree.add_message(["Durable", "Agile"], False, ["Light", "Heavy"])

    # layer 5
    tree.add_message(["Sabre", "https://robertsspaceindustries.com/pledge/ships/sabre/sabre"], True, ["Stealthy ?", "Not so much"])
    tree.add_message(["Scorpius", "Hurricane"], False, ["Stealthy ?", "Not so much"])

    # layer 6
    tree.add_message(["Scorpius", "https://robertsspaceindustries.com/pledge/ships/scorpius/Scorpius"], True, ["Scorpius", "Hurricane"])
    tree.add_message(["Hurricane", "https://robertsspaceindustries.com/pledge/ships/hurricane/Hurricane"], True, ["Scorpius", "Hurricane"])

    return tree

