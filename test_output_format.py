#!/usr/bin/env python3
"""
Quick test to show clean AI output format
Expected output with the optimized prompt
"""

test_output = """1. **What is this port?**
This is the door for FTP, which helps send and receive files over the internet. It's like a digital post office for your documents.

2. **Why is it risky?**
* Not always private: Your files and login details might not be scrambled, so others could snoop.
* Weak passwords: Often uses simple passwords that are easy for attackers to guess.
* Open to attack: If not protected well, hackers can steal, change, or delete your important files.

3. **How to secure it?**
* Close it down: If you don't use it, shut this port completely.
* Use a secure method: Switch to SFTP or FTPS, which always scramble your data.
* Strong passwords: Use long, unique, and complex passwords.
* Restrict who connects: Only allow specific, trusted people or computers to access it.

4. **Risk score:** HIGH"""

print("\n" + "="*70)
print("VulnX AI Analysis Output - Expected Format")
print("="*70 + "\n")
print(test_output)
print("\n" + "="*70)
print("✓ This is the clean, readable output you should see")
print("✓ No HTML tags visible")
print("✓ Numbered sections with bold headings")
print("✓ Bullet points with asterisks (*)")
print("✓ Simple, non-technical language")
print("✓ Risk score at the end")
print("="*70 + "\n")
