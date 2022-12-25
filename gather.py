import asyncio 
import aiohttp
import time

async def fetchFromGoogle():
    url='http://www.google.com'
    session=aiohttp.ClientSession()
    resp= await session.get(url)
    await resp.content.read()
    await session.close()
    
async def main():
    print(time.strftime('%X'))
    # asynornouhes 
    #await asyncio.gather(
    #    *[
    #        fetchFromGoogle() for _ in range(20)
    #    ]
    #)
    # synorhous routine
    for _ in range(20):
        await fetchFromGoogle()
    print (time.strftime('%X'))
if __name__=='__main__':
    asyncio.run(main())