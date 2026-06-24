#!/usr/bin/env python3
import os

with open('/Users/lipanovav/rag/03_MacDir/Mac/Loans/TEST/user_kvit.mac', 'rb') as f:
    raw = f.read()
text = raw.decode('cp866', errors='replace')
for i, line in enumerate(text.split('\n')[:80]):
    print(f"{i+1}: {line}")
