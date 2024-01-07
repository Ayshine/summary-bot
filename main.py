from interactions import SlashContext, slash_command
import interactions

bot = interactions.Client()

# Just to see the bot is ready
@interactions.listen()
async def on_startup():
    print("Bot is ready!")


@slash_command(
    name="summary",
    description="This will create a summary of the thread."
)
async def botSummary(ctx: SlashContext):  # Defines a new "context" (ctx) command called "summary".
        try:
            # Defer the response
            await ctx.defer()

            thread = ctx.channel
            
            messages = []
            # Fetch the history of the thread
            count = 0

            last_author = None
            async for message in thread.history(limit=None):

                # If the author is a bot, skip this message
                if message.author.bot:
                    continue

                # Get the message's creation time and format it as a string
                message_time = message.created_at.strftime("%Y-%m-%d %H:%M:%S")

                # Replace newline characters in the message content
                message_content = message.content.replace("\n", "")

                # Store the message, the author's name, and the creation time in the list
                messages.append({message_content})
                count += 1


            # Reverse the messages list
            messages.reverse()

            # Append the thread's title at the beginning of the list
            messages.insert(0, f'Thread Title: {thread.name}')

            print(messages)
            # Send a notification to the user who issued the command
            await ctx.send(f'{ctx.author.mention} your summary is being created. There are {count} messages at total here. This may take a while.') # you can make it hidden=True to hide the message

            # Here you can call your summary function with the messages list
            # summary(messages)
            # await ctx.send(f'{ctx.author.mention} Summary created! \n summary here....')

        except Exception as e:
            print(f"An error occurred: {e}")



bot.start("bot token here")


