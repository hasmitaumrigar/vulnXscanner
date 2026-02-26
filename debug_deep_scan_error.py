#!/usr/bin/env python3
"""
Debug test with full traceback
"""
import sys
import traceback
sys.path.insert(0, '/Users/utkarshraj/vulnXscanner/src')

from core.deep_subdomain_scanner import DeepSubdomainScanner

print("Debugging Deep Scan Error")
print("=" * 70)

domain = "google.com"
print(f"\nTesting {domain} with deep_scan=True\n")

try:
    scanner = DeepSubdomainScanner(domain, deep_scan=True)
    print(f"✅ Scanner created")
    print(f"   domain: {scanner.domain}")
    print(f"   deep_scan: {scanner.deep_scan}")
    print(f"   max_workers: {scanner.max_workers}\n")
    
    print("Calling scanner.scan()...")
    results = scanner.scan()
    
    print(f"✅ Results returned: {len(results)} subdomains")
    if results:
        print(f"   First: {results[0]}")
        
except Exception as e:
    print(f"\n❌ Exception occurred!")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"\nFull traceback:")
    traceback.print_exc()
