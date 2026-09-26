import asyncio


async def brew_tea():
    print("Brewing tea...")
    await asyncio.sleep(3)
    print("Tea brewed")


asyncio.run(brew_tea())
