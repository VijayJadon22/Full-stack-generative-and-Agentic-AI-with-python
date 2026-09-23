import asyncio


async def brew(name):
    print(f"Brewing {name} chai..")
    await asyncio.sleep(2)
    print(f"{name} chai is ready")


async def main():
    await asyncio.gather(brew("masala"), brew("green"), brew("ginger"))


asyncio.run(main())
