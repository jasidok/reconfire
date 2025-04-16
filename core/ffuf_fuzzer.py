# core/ffuf_fuzzer.py
import subprocess

def run_ffuf(input_file='outputs/gau_urls.txt', output_file='outputs/ffuf_results.txt'):
    wordlist = 'data/wordlist.txt'  # You can use SecLists or common.txt
    with open('tmp_ffuf_urls.txt', 'w') as f:
        for line in open(input_file):
            url = line.strip()
            if 'FUZZ' not in url:
                if url.endswith('/'):
                    f.write(f"{url}FUZZ\n")
                else:
                    f.write(f"{url}/FUZZ\n")
    cmd = f"ffuf -u FUZZ -w {wordlist} -of csv -mc 200,403,401 -input-cmd 'cat tmp_ffuf_urls.txt' -o {output_file}"
    subprocess.run(cmd, shell=True)

