import requests
import json
import discord

client = discord.Client()
TOKEN = 'BOT_TOKEN'
spoonacular = "API_KEY"
url = "https://api.spoonacular.com/recipes/"


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.help'):
        msg = ".random: random recipe"
        await message.channel.send(msg)

    if message.content.startswith('.random'):
        response = json.loads(requests.get(url + "random?apiKey=" + spoonacular).text)

        msg = response['recipes'][0]['image'] + "\n"
        msg += "Recipe: " + response['recipes'][0]['title'] + "\n"
        msg += "Link: " + response['recipes'][0]['sourceUrl'] + "\n"
        msg += "Servings: " + str(response['recipes'][0]['servings'])
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('BOT_TOKEN')