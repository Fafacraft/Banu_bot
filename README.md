# Discord_bot

This is a discord bot in relation to the game world of Star Citizen, specifically, the Banu.<br>
Talk like a Banu with $banu [message] !<br>
Alternatively, find your favorite ship with $ship.

Require :
- a bot token in token.txt
- pip install discord
- pip install nest_asyncio
- pip install pillow       with Raqm (libraqm) (as the Banu is a complex font to show)

# commandes
- $hello : send hi
- $banu [message] : translate SRB in ochoas  (see banu.md)

### discussion
- $ship : start the "finding a ship" discussion, following the tree in Ship_tree.txt
- $ship_find [ship] : search if [ship] is a possible ship from the ship discussion

### history
- $history @user : send command history of the user
- $last : send the last command sent
- $history_clear @user : clear user history



---
## sources
- general ; https://stackoverflow.com/
- generating images with text ; https://www.alpharithms.com/fit-custom-font-wrapped-text-image-python-pillow-552321/