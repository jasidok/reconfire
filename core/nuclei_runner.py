# core/nuclei_runner.py
import subprocess

def run_nuclei(input_file='outputs/httpx_results.txt', output_file='outputs/nuclei_output.txt'):
    domains = []
    with open(input_file, 'r') as f:
        for line in f:
            domain = line.strip().split()[0]
            if domain.startswith('http'):
                domains.append(domain)
            else:
                domains.append(f"http://{domain}")
    with open('tmp_nuclei.txt', 'w') as f:
        f.write('\n'.join(domains))
    cmd = f"nuclei -l tmp_nuclei.txt -severity low,medium,high,critical -o {output_file} -silent"
    subprocess.run(cmd, shell=True)

