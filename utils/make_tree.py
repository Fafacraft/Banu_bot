from custom_types.binary_tree import Discusion_tree, Node_tree

def make_tree():
    tree = Discusion_tree(["Small", "Big"]) #2/2

    # layer 1
    tree.add_message(["Military", "Civil", "sub1"], True, ["Small", "Big"]) #2/2
    tree.add_message(["Really Big ?", "Not that much"], False, ["Small", "Big"]) #2/2

    # layer 2
    tree.add_message(["Fighter", "Bomber"], True, ["Military", "Civil", "sub1"]) #2/2
    tree.add_message(["Versatile", "Specialized"], False, ["Military", "Civil", "sub1"]) #2/2
    
    tree.add_message(["Military", "Civil", "sub2"], True, ["Really Big ?", "Not that much"]) #2/2
    tree.add_message(["Military", "Civil", "sub3"], False, ["Really Big ?", "Not that much"]) #2/2

    # layer 3
    tree.add_message(["Light", "Heavy"], True, ["Fighter", "Bomber"]) #2/2
    tree.add_message(["In Space", "On Land", "sub1"], False, ["Fighter", "Bomber"]) #2/2
    tree.add_message(["Avengers Titan", "Cutlass"], True, ["Versatile", "Specialized"]) #2/2
    tree.add_message(["Transport", "Other", "sub1"], False, ["Versatile", "Specialized"]) #2/2
    
    tree.add_message(["Carrier", "Other"], True, ["Military", "Civil", "sub2"]) #2/2
    tree.add_message(["Luxe", "Industry"], False, ["Military", "Civil", "sub2"]) #2/2
    tree.add_message(["Bomber", "Other"], True, ["Military", "Civil", "sub3"]) #2/2
    tree.add_message(["Transport", "Other", "sub2"], False, ["Military", "Civil", "sub3"]) #2/2

    # layer 4
    tree.add_message(["Stealthy ?", "Not so much"], True, ["Light", "Heavy"]) #2/2
    tree.add_message(["Durable", "Agile"], False, ["Light", "Heavy"]) #2/2
    tree.add_message(["Eclipse", "https://robertsspaceindustries.com/pledge/ships/eclipse/Eclipse"], True, ["In Space", "On Land", "sub1"]) #0/0
    tree.add_message(["Spirit A1", "https://robertsspaceindustries.com/pledge/ships/spirit/A1-Spirit"], False, ["In Space", "On Land", "sub1"]) #0/0
    tree.add_message(["Avengers Titan", "https://robertsspaceindustries.com/pledge/ships/aegis-avenger/Avenger-Titan"], True, ["Avengers Titan", "Cutlass"]) #0/0
    tree.add_message(["Cutlass", "https://robertsspaceindustries.com/pledge/ships/drake-cutlass/Cutlass-Black"], False, ["Avengers Titan", "Cutlass"]) #0/0
    tree.add_message(["Hull-A", "Spirit C1"], True, ["Transport", "Other", "sub1"]) #2/2
    tree.add_message(["Industry", "Racing"], False, ["Transport", "Other", "sub1"]) #2/2
    
    tree.add_message(["Kraken", "Bengal"], True, ["Carrier", "Other"]) #2/2
    tree.add_message(["Javelin", "Idris"], False, ["Carrier", "Other"]) #2/2
    tree.add_message(["Tourism", "Merchant"], True, ["Luxe", "Industry"]) #2/2
    tree.add_message(["Mining", "Transport"], False, ["Luxe", "Industry"]) #2/2
    tree.add_message(["In Space", "On Land", "sub2"], True, ["Bomber", "Other"]) #2/2
    tree.add_message(["Gunship", "Troop Transport"], False, ["Bomber", "Other"]) #2/2
    tree.add_message(["Passenger", "Cargo"], True, ["Transport", "Other", "sub2"]) #2/2
    tree.add_message(["Versatile", "Other"], False, ["Transport", "Other", "sub2"]) #2/2


    # layer 5
    tree.add_message(["Sabre", "https://robertsspaceindustries.com/pledge/ships/sabre/sabre"], True, ["Stealthy ?", "Not so much"]) #0/0
    tree.add_message(["Arrow", "Gladius"], False, ["Stealthy ?", "Not so much"]) #2/2
    tree.add_message(["Vanguard", "https://robertsspaceindustries.com/pledge/ships/vanguard/Vanguard-Warden"], True, ["Durable", "Agile"]) #0/0
    tree.add_message(["Scorpius", "Hurricane"], False, ["Durable", "Agile"]) #2/2
    tree.add_message(["Hull-A", "https://robertsspaceindustries.com/pledge/ships/hull/Hull-A"], True, ["Hull-A", "Spirit C1"]) #0/0
    tree.add_message(["Spirit C1", "https://robertsspaceindustries.com/pledge/ships/spirit/C1-Spirit"], False, ["Hull-A", "Spirit C1"]) #0/0
    tree.add_message(["Mining", "Other"], True, ["Industry", "Racing"]) #2/2
    tree.add_message(["M50", "Razor"], False, ["Industry", "Racing"]) #2/2

    tree.add_message(["Kraken", "https://robertsspaceindustries.com/pledge/ships/drake-kraken/Kraken"], True, ["Kraken", "Bengal"]) #0/0
    tree.add_message(["Bengal", "https://starcitizen.tools/Bengal"], True, ["Kraken", "Bengal"]) #0/0
    tree.add_message(["Javelin", "https://robertsspaceindustries.com/pledge/ships/aegis-javelin/Javelin"], True, ["Javelin", "Idris"]) #0/0
    tree.add_message(["Idris", "https://robertsspaceindustries.com/pledge/ships/aegis-idris/Idris-P"], False, ["Javelin", "Idris"]) #0/0
    tree.add_message(["890 Jump", "https://robertsspaceindustries.com/pledge/ships/890-jump/890-Jump"], True, ["Tourism", "Merchant"]) #0/0
    tree.add_message(["Merchantman", "https://robertsspaceindustries.com/pledge/ships/merchantman/Merchantman"], False, ["Tourism", "Merchant"]) #0/0
    tree.add_message(["Orion", "https://robertsspaceindustries.com/pledge/ships/orion/Orion"], True, ["Mining", "Transport"]) #0/0
    tree.add_message(["Hull-E", "https://robertsspaceindustries.com/pledge/ships/hull/Hull-E"], False, ["Mining", "Transport"]) #0/0
    tree.add_message(["Retaliator", "https://robertsspaceindustries.com/pledge/ships/aegis-retaliator/Retaliator"], True, ["In Space", "On Land", "sub2"]) #0/0
    tree.add_message(["A2", "https://robertsspaceindustries.com/pledge/ships/crusader-starlifter/A2-Hercules"], False, ["In Space", "On Land", "sub2"]) #0/0
    tree.add_message(["Hammerhead", "Redeemer"], True, ["Gunship", "Troop Transport"]) #2/2
    tree.add_message(["M2", "Valkyrie"], False, ["Gunship", "Troop Transport"]) #2/2
    tree.add_message(["Genesis Starliner", "600i"], True, ["Passenger", "Cargo"]) #2/2
    tree.add_message(["C2", "Hull-C"], False, ["Passenger", "Cargo"]) #2/2
    tree.add_message(["Constellation", "Carrack"], True, ["Versatile", "Other"]) #2/2
    tree.add_message(["Exploration", "Industry"], False, ["Versatile", "Other"]) #2/2

    # layer 6
    tree.add_message(["Arrow", "https://robertsspaceindustries.com/pledge/ships/anvil-arrow/Arrow"], True, ["Arrow", "Gladius"]) #0/0
    tree.add_message(["Gladius", "https://robertsspaceindustries.com/pledge/ships/gladius/Gladius"], False, ["Arrow", "Gladius"]) #0/0
    tree.add_message(["Scorpius", "https://robertsspaceindustries.com/pledge/ships/scorpius/Scorpius"], True, ["Scorpius", "Hurricane"]) #0/0
    tree.add_message(["Hurricane", "https://robertsspaceindustries.com/pledge/ships/hurricane/Hurricane"], False, ["Scorpius", "Hurricane"]) #0/0
    tree.add_message(["Prospector", "https://robertsspaceindustries.com/pledge/ships/misc-prospector/Prospector"], True, ["Mining", "Other"]) #0/0
    tree.add_message(["SRV", "https://robertsspaceindustries.com/pledge/ships/argo-srv/SRV"], False, ["Mining", "Other"]) #0/0
    tree.add_message(["M50", "https://robertsspaceindustries.com/pledge/ships/origin-m50/M50"], True, ["M50", "Razor"]) #0/0
    tree.add_message(["Razor", "https://robertsspaceindustries.com/pledge/ships/razor/Razor"], False, ["M50", "Razor"]) #0/0

    tree.add_message(["Hammerhead", "https://robertsspaceindustries.com/pledge/ships/hammerhead/Hammerhead-Best-In-Show-Edition"], True, ["Hammerhead", "Redeemer"]) #0/0
    tree.add_message(["Redeemer", "https://robertsspaceindustries.com/pledge/ships/redeemer/Redeemer"], False, ["Hammerhead", "Redeemer"]) #0/0
    tree.add_message(["M2", "https://robertsspaceindustries.com/pledge/ships/crusader-starlifter/M2-Hercules"], True, ["M2", "Valkyrie"]) #0/0
    tree.add_message(["Valkyrie", "https://robertsspaceindustries.com/pledge/ships/anvil-valkyrie/Valkyrie"], False, ["M2", "Valkyrie"]) #0/0
    tree.add_message(["Genesis Starliner", "https://robertsspaceindustries.com/pledge/ships/starliner/Genesis"], True, ["Genesis Starliner", "600i"]) #0/0
    tree.add_message(["600i", "https://robertsspaceindustries.com/pledge/ships/600i/600i-Touring"], False, ["Genesis Starliner", "600i"]) #0/0
    tree.add_message(["C2", "https://robertsspaceindustries.com/pledge/ships/crusader-starlifter/C2-Hercules"], True, ["C2", "Hull-C"]) #0/0
    tree.add_message(["Hull-C", "https://robertsspaceindustries.com/pledge/ships/hull/Hull-C"], False, ["C2", "Hull-C"]) #0/0
    tree.add_message(["Constellation", "https://robertsspaceindustries.com/pledge/ships/rsi-constellation/Constellation-Aquila"], True, ["Constellation", "Carrack"]) #0/0
    tree.add_message(["Carrack", "https://robertsspaceindustries.com/pledge/ships/carrack/Carrack-Expedition"], False, ["Constellation", "Carrack"]) #0/0
    tree.add_message(["400i", "Corsair"], True, ["Exploration", "Industry"]) #2/2
    tree.add_message(["Mole", "https://robertsspaceindustries.com/pledge/ships/argo-mole/MOLE"], False, ["Exploration", "Industry"]) #0/0

    # layer 7
    tree.add_message(["400i", "https://robertsspaceindustries.com/pledge/ships/400i/400i"], True, ["400i", "Corsair"]) #0/0
    tree.add_message(["Corsair", "https://robertsspaceindustries.com/pledge/ships/drake-corsair/Corsair"], False, ["400i", "Corsair"]) #0/0

    return tree

