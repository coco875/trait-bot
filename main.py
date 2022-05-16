import discord
import random

client = discord.Client()

with open("trait de personnalité.txt", "r", encoding="utf-8") as f:
    trait = f.read()
    trait = trait.split("\n")
    for i in trait:
        trait[trait.index(i)] = i.split(" / ")

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

print(trait)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def check_double(rep):
    for i in rep:
            if len(i)>1:
                for j in rep:
                    if i[1] in j and i[0] != j[0]:
                        rep.remove(i)
                        rep.append(random.choice(trait))
                        print("ok")
                        return check_double(rep)
    return rep

@client.event
async def on_message(message):
    if message.content.startswith('!trait'):
        rep = [random.choice(trait) for i in range(3)]
        rep = check_double(rep)
        print(rep)
        await message.reply(rep[0][0] + "\n" + rep[1][0] + "\n" + rep[2][0])
    
    if message.author.id == 324941472367640596:
        if message.content.startswith("!role trait"):
            await message.guild.create_role(name="Trait")

client.run(token)