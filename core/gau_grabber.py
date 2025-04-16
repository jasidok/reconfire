# core/gau_grabber.py
import subprocess
import os

def run_gau(input_file='outputs/httpx_results.txt', output_file='outputs/gau_urls.txt'):
    domains = []
    with open(input_file, 'r') as f:
        for line in f:
            domain = line.strip().split()[0]
            if domain.startswith('http'):
                domains.append(domain.replace('http://', '').replace('https://', ''))
    with open('tmp_httpx_domains.txt', 'w') as f:
        f.write('\n'.join(domains))
    cmd = f"cat tmp_httpx_domains.txt | gau --threads 50 > {output_file}"
    os.system(cmd)
    os.remove('tmp_httpx_domains.txt')

