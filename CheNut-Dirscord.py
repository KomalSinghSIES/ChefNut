import discord
from discord.ext import commands
import requests
import json
import os

client = commands.Bot(command_prefix=".")

os.chdir(r'C:\Users\Kumar\PycharmProjects\ChefNut\venv')

with open('data/api_key.json', 'r') as f:
    api_key = json.load(f)

@client.command()
@commands.cooldown(2, 1, commands.BucketType.default)
async def food(ctx, item_name):

    r = requests.get(f"https://api.nutritionix.com/v1_1/search/{item_name}?results=0:20&fields=item_name,brand_name,nf_iron_dv,nf_calories,nf_total_fat,nf_cholesterol,nf_sodium,nf_serving_weight_grams,nf_protein,nf_sugars,nf_calcium_dv&appId=APP_ID&appKey=APP_KEY")
    json_data = r.json()
    item_name = json_data['hits'][0]['fields']['item_name']
    brand_name = json_data['hits'][0]['fields']['brand_name']
    nf_iron_dv = json_data['hits'][0]['fields']['nf_iron_dv']
    nf_calories = json_data['hits'][0]['fields']['nf_calories']
    nf_total_fat = json_data['hits'][0]['fields']['nf_total_fat']
    nf_cholesterol = json_data['hits'][0]['fields']['nf_cholesterol']
    nf_sodium = json_data['hits'][0]['fields']['nf_sodium']
    # nf_total_carbohydrate = json_data['hits'][0]['fields']['nf_total_carbohydrate']
    nf_serving_weight_grams = json_data['hits'][0]['fields']['nf_serving_weight_grams']
    # nf_potassium = json_data['hits'][0]['fields']['nf_potassium']
    nf_protein = json_data['hits'][0]['fields']['nf_protein']
    nf_sugars = json_data['hits'][0]['fields']['nf_sugars']
    nf_calcium_dv = json_data['hits'][0]['fields']['nf_calcium_dv']
    #description = json_data['brand_name']['item_id']['nf_calories']
    #print(item_name,description)

    embed = discord.Embed(
        title="Food Nutrients",
        #description=f"{item_name.upper()}",
        color=discord.Color.dark_blue()
    )

    embed.add_field(name="item_name", value=item_name, inline=False)
    embed.add_field(name="brand_name", value=f"{brand_name}\u2109", inline=False)
    embed.add_field(name="nf_iron_dv", value=f"{nf_iron_dv}\u2109", inline=False)
    embed.add_field(name="nf_calories", value=f"{nf_calories}\u2109", inline=False)
    embed.add_field(name="nf_total_fat", value=f"{nf_total_fat}\u2109", inline=False)
    embed.add_field(name="nf_cholesterol", value=f"{nf_cholesterol}\u2109", inline=False)
    embed.add_field(name="nf_sodium", value=f"{nf_sodium}\u2109", inline=False)
    # embed.add_field(name="nf_total_carbohydrate", value=f"{nf_total_carbohydrate}\u2109", inline=False)
    embed.add_field(name="nf_serving_weight_grams", value=f"{nf_serving_weight_grams}\u2109", inline=False)
    # embed.add_field(name="nf_potassium", value=f"{nf_potassium}\u2109", inline=False)
    embed.add_field(name="nf_protein", value=f"{nf_protein}\u2109", inline=False)
    embed.add_field(name="nf_sugars", value=f"{nf_sugars}\u2109", inline=False)
    embed.add_field(name="nf_calcium_dv", value=f"{nf_calcium_dv}\u2109", inline=False)


    await ctx.send(embed=embed)

@food.error
async def foodnut_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("This command is on cooldown.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("That is not a valid name.")


client.run('BOT_TOKEN')

if name == 'main':
  main()