import asyncio
import io
import discord
import nest_asyncio
from discord.ext import commands
from custom_types.hashmap import Hashmap
from custom_types.chained_list import chained_list
from custom_types.binary_tree import Discusion_tree
from utils.make_tree import make_tree
from utils.image import makeBanuTextImg

nest_asyncio.apply()


intents = discord.Intents.all() # LES DROITS

client = commands.Bot(command_prefix="$", intents = intents)

# START OF CODE

history = Hashmap(1000)
last_command = " "
ship_tree = make_tree()


def append_command(ctx):
  global last_command
  global history
  key = ctx.author.mention
  user_history = history.get(key)
  last_command = str(ctx.message.created_at) + " : " + ctx.message.content + " by " + ctx.message.author.global_name
  if user_history == None:
    history.set(key, chained_list())
    user_history = history.get(key)
  user_history.append(ctx.message)
  

# show last command
@client.command(name="last")
async def last_commande(ctx):
  global last_command
  await ctx.send(last_command)
  append_command(ctx) # at the end so it doesn't send itself :P

# show history
@client.command(name="history")
async def show_history(ctx, arg1):
  global history
  append_command(ctx)
  user_history = history.get(arg1)
  if user_history == None:
    await ctx.send("No history")
    return
  for i in range (user_history.length()):
    msg = user_history.get(i)
    await ctx.send(str(msg.created_at) + " : " + msg.content + " by " + msg.author.global_name)

# clear history
@client.command(name="history_clear")
async def history_clear(ctx, arg1):
  global history
  history.set(arg1, None)
  append_command(ctx)


# start ship discussion
@client.command(name="ship")
async def ship_discussion(ctx):
  global ship_tree

  # if leaf, found the ship, send the right message and skip the else
  if (ship_tree.isAtLeaf()):
    await ctx.message.reply("""
# This is your ship ; 
                                     
Name : """ + ship_tree.get_current()[0] + """
Link : """ + ship_tree.get_current()[1] + """
""")


  # else, we're still in the discussion
  else:
    response = await ctx.message.reply("""
# What Star Citizen fits you the best ! 
                                  
1️⃣ : """ + ship_tree.get_current()[0] + """
2️⃣ : """ + ship_tree.get_current()[1] + """
🔄 : reset
❌ : cancel
""")
    
    # add reactions
    await response.add_reaction("1️⃣")
    await response.add_reaction("2️⃣")
    await response.add_reaction("🔄")
    await response.add_reaction("❌")
    
    # check used to listen to reaction_add
    def check(reaction, user):
      emoji_list = ['1️⃣', '2️⃣', '🔄', '❌']
      return user == ctx.message.author and str(reaction.emoji) in emoji_list
    
    try:
      # do the thing when reaction is clicked
      reaction, user = await client.wait_for('reaction_add', timeout=120.0, check=check)
      match reaction.emoji:
        case '1️⃣':
          # go to the True node and let's go for another round
          ship_tree.next_node(True)
          await ship_discussion(ctx)
          return
        case '2️⃣':
          # go to the False node and let's go for another round
          ship_tree.next_node(False)
          await ship_discussion(ctx)
          return
        case '🔄':
          # reset and let's go for another round
          ship_tree.current_node = ship_tree.root
          await ship_discussion(ctx)
          return
        case '❌':
          await ctx.send("Cancelled")
          pass
          
    # if it's timed out, will go out of discussion
    except asyncio.TimeoutError:
      await ctx.send("Idle for too long ; conversation stopped.")
  # end of else, out of discussion
  
  
  # reset the tree for next time, and stop the conversation
  ship_tree.current_node = ship_tree.root
  append_command(ctx)
  return


# search if the arg is a ship we can get in our discussion tree
@client.command(name="ship_find")
async def hello(ctx, arg1):
  append_command(ctx)
  if (ship_tree.isThereShip(arg1, ship_tree.root)):
    await ctx.send("This ship can be found")
  else:
    await ctx.send("This ship cannot be found")

# send Hi
@client.command(name="hello")
async def hello(ctx):
  append_command(ctx)
  await ctx.send(" Hi")

@client.command(name="banu")
async def toBanu(ctx, *, msg: str):
  append_command(ctx)
  img = makeBanuTextImg(msg)
  
  # create buffer
  buffer = io.BytesIO()
  # save PNG in buffer
  img.save(buffer, format="PNG")
  # move to beginning of buffer so `send()` it will read from beginning
  buffer.seek(0)
  await ctx.send(ctx.author.mention + " : ", file=discord.File(buffer, 'banu.png'))

  # so we can't cheat, you need to know how to read banu :)
  await ctx.message.delete()




@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044900412551073832)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@client.event
async def on_message(message):
  # if it's himself
  if message.author == client.user:
    return

  await client.process_commands(message)



# END OF CODE

with open('token.txt', 'r') as file:
  file_content = file.read()
  if file_content == "":
    print("No token")
  else:
    client.run(file_content)