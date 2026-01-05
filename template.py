from pathlib import Path

# Root directory (current folder)
ROOT_DIR = Path(".")

# Folder structure
folders = [
    "config",
    "data/resumes",
    "embeddings",
    "loaders",
    "llm",
    "agents",
    "tools",
    "utils",
]

# Files to create
files = {
    "app.py": "# Streamlit entry point\n",
    "config/settings.py": "# API keys and model configurations\n",
    "embeddings/vector_store.py": "# FAISS / Chroma vector store logic\n",
    "loaders/resume_loader.py": "# Resume loading and chunking logic\n",
    "llm/mistral_client.py": "# Mistral AI client wrapper\n",
    "agents/resume_agent.py": "# Agent logic for resume analysis\n",
    "tools/resume_search_tool.py": "# Resume search tool for agent\n",
    "utils/logger.py": "# Custom logger utility\n",
    "requirements.txt": "",
    "README.md": "# Resume Analyzer Agentic AI POC\n",
}

def create_structure():
    # Create folders
    for folder in folders:
        path = ROOT_DIR / folder
        path.mkdir(parents=True, exist_ok=True)

    # Create files
    for file_path, content in files.items():
        path = ROOT_DIR / file_path
        if not path.exists():
            path.write_text(content)

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
