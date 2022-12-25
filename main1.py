#synochrous funtiomn

import asyncio
import time
async def waiter(n):
    await asyncio.sleep(n)
    print(f"waited for {n} seocnds")
    
async def main():
    print(time.strftime('%X'))
    await waiter(2)
    await waiter(3)  
    print(time.strftime('%X'))
    
if __name__== '__main__':
    asyncio.run(main())