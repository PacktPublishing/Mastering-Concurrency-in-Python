import asyncio
import aiohttp

async def get_html(session, url):
    async with session.get(url) as res:
        return await res.text()

async def main():
    urls = [
        'http://python.org',
        'http://google.com',
        ''
    ]

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        html = await get_html(session, 'http://python.org')
        print(len(html))

asyncio.run(main())
