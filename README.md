# 🚀 MockPipeline

**MockPipeline** is a simple educational Python package that simulates a document processing pipeline with steps like downloading, archiving, uploading, extracting, and classifying.

> This is built for educational purposes and is intended to demonstrate how to structure and publish a Python package with a command-line interface (CLI).

---

## 📦 Features

- Modular pipeline steps (download, archive, upload, extract, classify)
- Clean CLI interface: run everything using one command
- Installable via GitHub
- Built using `pyproject.toml` (PEP 621 compliant)

---

## 🔧 Installation

You can install this package directly from GitHub using:

```bash
pip install git+https://github.com/yasandu0505/python-package.git
```

> ⚠️ If installed with `--user`, make sure your Python user scripts directory is in your PATH:
>
> For example:
> ```bash
> export PATH="$HOME/Library/Python/3.9/bin:$PATH"
> ```

---

## 🚀 Usage

After installation, you can run the pipeline using the command-line tool:

```bash
mock-project --year 2024 --lang en
```

### 🔹 CLI Arguments

| Argument   | Required | Description                       |
|------------|----------|-----------------------------------|
| `--year`   | ✅ Yes    | Year of documents to process      |
| `--lang`   | ❌ No     | Language of documents (default: `en`) |

---

## 🧠 Example Output

```
Starting mock pipeline for year 2024 and language en
📥 Downloading documents...
📦 Archiving documents...
☁️ Uploading to cloud...
📄 Extracting text from documents...
🧠 Classifying documents...
✅ Pipeline complete.
```

---

## 📁 Project Structure

```
mockpipeline/
├── __init__.py
├── main.py
└── steps/
    ├── archive.py
    ├── classify.py
    ├── download.py
    ├── extract.py
    └── upload.py
```

---

## 💡 Educational Purpose

This repository is ideal for learning about:

- Python packaging with `pyproject.toml`
- Command-line applications using `argparse`
- Code organization into modules
- Using GitHub as a package source

---

## 👤 Author

**Yasandu Imanjith**  
📫 [yasandu0505](https://github.com/yasandu0505)

---

