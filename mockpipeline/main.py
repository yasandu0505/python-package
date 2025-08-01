from .steps.download import download_documents
from .steps.archive import archive_documents
from .steps.upload import upload_documents
from .steps.extract import extract_documents
from .steps.classify import classify_documents

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--lang', type=str, default='en')
    args = parser.parse_args()

    print(f"Starting mock pipeline for year {args.year} and language {args.lang}")
    download_documents()
    archive_documents()
    upload_documents()
    extract_documents()
    classify_documents()
    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
