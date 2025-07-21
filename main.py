# main.py
import os
import subprocess
import tempfile
import shutil
import json
from analyze.complexity_analyzer import run_lizard
from analyze.vulnerability_analyzer import run_semgrep
from llm.gemini_api import get_model, prompt_gemini_for_complexity, prompt_gemini_for_vulnerability
from utils.repo_handler import clone_repo, extract_code_from_file


def main():
    repo_url = input("Enter GitHub repository URL: ").strip()
    model = get_model()
    local_path = clone_repo(repo_url)


    # --- Code Smells / Complexity ---
    complexity = run_lizard(local_path)
    for func in complexity[:3]:
        code = extract_code_from_file(
            func['file'], func['start_line'], func['end_line'])
        print(f"\n🧠 Complex Function: {func['name']} in {func['file']}")
        print(prompt_gemini_for_complexity(model, code, func))

    # --- Vulnerability Detection ---
    semgrep_result = run_semgrep(local_path)
    findings = semgrep_result.get("results", [])[:5]
    for finding in findings:
        file_path = finding["path"]
        start = finding["start"]["line"]
        end = finding["end"]["line"]
        message = finding["extra"]["message"]
        code = extract_code_from_file(
            os.path.join(local_path, file_path), start, end)

        print(f"\n🔐 Vulnerability in {file_path}:{start}-{end}")
        print(f"📋 Semgrep: {message}")
        print(prompt_gemini_for_vulnerability(model, code, message))

    shutil.rmtree(local_path)


if __name__ == "__main__":
    main()
