# another_script.py
from mockpipeline.main import main

# Simulate running with command-line arguments
import sys
sys.argv = ["mock-project", "--year", "2025", "--lang", "si"]

main()
