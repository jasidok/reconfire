import subprocess
def run_subfinder(input_file, out_dir):
    output = f"{out_dir}/subfinder.txt"
    cmd = f"subfinder -dL {input_file} -silent -o {output}"
    subprocess.run(cmd, shell=True)
    return output

