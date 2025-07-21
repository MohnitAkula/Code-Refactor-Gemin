# Code Refactor using Gemini 2.5 Pro

NebulaAI is a code intelligence tool that uses **Gemini (Google's LLM)** and **Semgrep** to detect and automatically refactor code smells, performance bottlenecks, and security vulnerabilities across repositories.

---

## 🔧 Features

- ⚡ Clone and scan any public GitHub repository
- 🧠 Use Gemini Pro to suggest and apply code improvements
- 🔍 Detect security issues, bugs, and code smells with Semgrep
- 🛠️ Modular pipeline for easy integration into CI/CD workflows

---
## Instructions
- Set-up Google api key as an environment variable as GOOGLE_API_KEY=your_api_key
- Run requirements.txt with pip install -r requirements.txt
- Make a Semgrep account and then run semgrep login after running requirements.txt
  
## 📁 Project Structure

```bash
Code-Refactor-Gemini/
│
├── main.py                 # Entry point
├── utils/
│   ├── repo_handler.py     # Clone & manage GitHub repositories
│   ├── analyzer.py         # Semgrep & Gemini integration
│   └── file_utils.py       # File read/write utilities
├── .env                    # (Optional) Contains GOOGLE_API_KEY
└── README.md               # You're reading it!

'''

