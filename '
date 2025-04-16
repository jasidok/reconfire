# main.py
import asyncio
from core.feeder import chunk_and_feed
from core.httpx_probe import run_httpx_probe
from core.gau_grabber import run_gau
from core.nuclei_runner import run_nuclei
from core.ffuf_fuzzer import run_ffuf

def run_pipeline(target_file='data/in_scope_subs.txt'):
    chunk_and_feed(target_file)
    asyncio.run(run_httpx_probe())
    run_gau()
    run_nuclei()
    run_ffuf()

if __name__ == "__main__":
    run_pipeline()

