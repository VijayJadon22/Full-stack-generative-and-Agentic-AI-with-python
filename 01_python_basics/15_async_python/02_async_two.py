import asyncio
import time


async def brew(name):
    print(f"Brewing {name} chai..")
    await asyncio.sleep(2)
    # time.sleep(2) #time,sleep will have to wait after each command or call
    print(f"{name} chai is ready")


async def main():
    await asyncio.gather(brew("masala"), brew("green"), brew("ginger"))


asyncio.run(main())
