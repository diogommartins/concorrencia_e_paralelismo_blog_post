import asyncio
from aiohttp import ClientSession


async def get_and_print(loop):
    async with ClientSession(loop=loop) as session:
        async with session.get("http://www.americanas.com") as response:
            print(await response.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(get_and_print(loop))
