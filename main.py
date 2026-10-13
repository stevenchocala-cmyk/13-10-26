import discord
from discord.ext import commands
from model import predict_image
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def predict(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image for prediction.")
        return

    attachment = ctx.message.attachments[0]
    image_path = f"temp_{attachment.filename}"
    await attachment.save(image_path)

    model_path = "keras_model.h5"  # Path to your trained model
    labels_path = "labels.txt"  # Path to your labels file

    try:
        predict_image(model_path, labels_path, image_path)
        await ctx.send("Prediction completed. Check the console for results.")
    except Exception as e:
        await ctx.send(f"An error occurred during prediction: {e}")



