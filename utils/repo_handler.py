import os
import tempfile
import subprocess
import shutil


def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    subprocess.run(["git", "clone", repo_url, temp_dir], check=True)
    return temp_dir


def extract_code_from_file(file_path, start_line, end_line):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        return ''.join(lines[start_line-1:end_line])
