import asyncio
from aiohttp import ClientSession

urls = (
    'http://www.americanas.com',
    'http://www.submarino.com',
    'http://www.shoptime.com',
    'http://www.soubarato.com',
)


async def get_and_print(session, url):
    async with session.get(url) as response:
        print(await response.text())


async def fetch(loop, urls):
    async with ClientSession(loop=loop) as session:
        tasks = (get_and_print(session, url) for url in urls)
        await asyncio.gather(*tasks, return_exceptions=True)
        loop.stop()

loop = asyncio.get_event_loop()
loop.create_task(fetch(loop, urls))
loop.run_forever()
