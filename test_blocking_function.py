#!/usr/bin/env python3
"""
Test to check what scan_subdomains_blocking returns
"""
import sys
sys.path.insert(0, '/Users/utkarshraj/vulnXscanner/src')

from core.deep_subdomain_scanner import scan_subdomains_blocking

print("Testing scan_subdomains_blocking function")
print("=" * 70)

# Test 1: Simple mode
print("\n1️⃣ Testing SIMPLE MODE (deep_scan=False):")
print("-" * 70)
results_simple = scan_subdomains_blocking("google.com", deep_scan=False)
print(f"Type: {type(results_simple)}")
print(f"Count: {len(results_simple)}")
if results_simple:
    print(f"First result: {results_simple[0]}")
else:
    print("❌ No results returned!")

# Test 2: Deep mode
print("\n2️⃣ Testing DEEP MODE (deep_scan=True):")
print("-" * 70)
results_deep = scan_subdomains_blocking("google.com", deep_scan=True)
print(f"Type: {type(results_deep)}")
print(f"Count: {len(results_deep)}")
if results_deep:
    print(f"First result: {results_deep[0]}")
else:
    print("❌ No results returned!")

print("\n" + "=" * 70)
if results_simple:
    print(f"✅ Simple mode works: {len(results_simple)} subdomains")
else:
    print(f"❌ Simple mode failed")

if results_deep:
    print(f"✅ Deep mode works: {len(results_deep)} subdomains")
else:
    print(f"❌ Deep mode failed")
