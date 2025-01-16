import asyncio

async def print_messages():
    print("Message 1")
    await asyncio.sleep(1)
    print("Message 2")

# Run the asynchronous function
asyncio.run(print_messages())
