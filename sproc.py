#!/bin/env python
import subprocess

obj = subprocess.run(["cat"],stdout=subprocess.PIPE,input="\nsproc.py",text=True)
print(f"output: {obj.stdout}")
