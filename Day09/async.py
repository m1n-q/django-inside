import asyncio

async def num():
    for i in range(5):
        print('[ %d ]' %i)

async def alpha():
    for i in 'ABC':
        await num()
        print('< %s >' %i)

async def main():
    await alpha()
asyncio.run(main())
