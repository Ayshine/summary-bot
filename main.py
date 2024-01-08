from interactions import SlashContext, slash_command
import interactions
from summary import summarize
import time


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
        start_time = time.time()

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
                # message_time = message.created_at.strftime("%Y-%m-%d %H:%M:%S")

                # Replace newline characters in the message content
                message_content = message.content.replace("\n", "")

                # Store the message, the author's name, and the creation time in the list
                messages.append(message_content)
                count += 1


            # Reverse the messages list
            messages.reverse()

            # Append the thread's title at the beginning of the list
            messages.insert(0, f"Bu thread'i özetler misin?. 'Thread Title: {thread.name}'")

            print(messages)
            # Send a notification to the user who issued the command
            await ctx.send(f'{ctx.author.mention} your summary is being created. There are {count} messages at total here. This may take a while.') # you can make it hidden=True to hide the message

            # # Here you can call your summary function with the messages list
            summary = summarize(messages)

            # Clear the messages list
            messages.clear()

            await ctx.send(f'{ctx.author.mention} Summary created! \n Summary HEREEEEE: {summary}')

            print(f"Summary HEREEEEE: {summary}")



            end_time = time.time()
            execution_time = end_time - start_time
            print(f"The code executed in {execution_time} seconds for {count} messages")
            
        except Exception as e:
            print(f"An error occurred: {e}")



bot.start("MTE4MzU1NDY5MzM5ODUyODA1MQ.GO9rY5.3EqjAjGxQgEyYnIDSFpNoo7EeVLlSu1vkBB2rY")



