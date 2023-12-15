import discord
import nest_asyncio
from discord.ext import commands
from custom_types.hashmap import Hashmap
from custom_types.chained_list import chained_list
from custom_types.binary_tree import Discusion_tree

nest_asyncio.apply()


intents = discord.Intents.all() # LES DROITS

client = commands.Bot(command_prefix="$", intents = intents)

# START OF CODE


history = Hashmap(1000)
last_command = " "

def append_command(ctx):
  global last_command
  global history
  print(ctx.author.mention)
  key = ctx.author.mention
  user_history = history.get(key)
  print(last_command)
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

# send Hi
@client.command(name="hello")
async def hello(ctx):
  append_command(ctx)
  await ctx.send("Hi")



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