import redis

def chunk_and_feed(input_file='targets.txt', chunk_size=10000):
    r = redis.Redis()
    chunk = []
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            domain = line.strip()
            if not domain:
                continue
            chunk.append(domain)
            if len(chunk) >= chunk_size:
                for d in chunk:
                    r.rpush('domain_queue', d)
                print(f"[+] Chunk pushed: {i+1}")
                chunk = []
        # Final leftovers
        if chunk:
            for d in chunk:
                r.rpush('domain_queue', d)

