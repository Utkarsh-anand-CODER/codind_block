#asynochronous funtion
import asyncio
import time
async def waiter(n):
    await asyncio.sleep(n)
    print(f"waited for {n} seocnds")
    
async def main():
    # Event loop
    task1=asyncio.create_task(waiter(2))
    task2=asyncio.create_task(waiter(3))
    
    print(time.strftime('%X'))
    await task1
    await task2
    print(time.strftime('%X'))

if __name__== '__main__':
    asyncio.run(main())