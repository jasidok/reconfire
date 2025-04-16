# core/httpx_probe.py

import aiohttp
import asyncio
import aioredis
from rich.console import Console

console = Console()

async def probe_domain(session, domain):
    try:
        url = f"http://{domain}"
        async with session.get(url, timeout=5) as resp:
            text = await resp.text()
            title = text.split('<title>')[1].split('</title>')[0] if '<title>' in text else ''
            return domain, resp.status, title
    except:
        return domain, None, None

async def worker(redis, output_file):
    async with aiohttp.ClientSession() as session:
        while True:
            domain = await redis.lpop('domain_queue')
            if not domain:
                await asyncio.sleep(1)
                continue
            domain = domain.decode()
            d, status, title = await probe_domain(session, domain)
            if status and status in [200, 301, 302]:
                console.log(f"[+] {d} [{status}] {title}")
                with open(output_file, 'a') as f:
                    f.write(f"{d} [{status}] {title}\n")

async def run_httpx_probe(output_file='outputs/httpx_results.txt', threads=50):
    redis = await aioredis.from_url("redis://localhost")
    workers = [asyncio.create_task(worker(redis, output_file)) for _ in range(threads)]
    await asyncio.gather(*workers)

