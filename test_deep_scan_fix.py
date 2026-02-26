#!/usr/bin/env python3
"""
Test script to verify deep scan bug fixes
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_deep_scan_fix():
    """Test that deep scan now finds subdomains"""
    from core.deep_subdomain_scanner import DeepSubdomainScanner
    
    print("=" * 70)
    print("Testing Deep Scan Bug Fixes")
    print("=" * 70)
    
    # Test with a well-known domain
    test_domain = "google.com"
    
    print(f"\n🧪 Testing Deep Scan with {test_domain}...")
    print("-" * 70)
    
    scanner = DeepSubdomainScanner(test_domain, deep_scan=True)
    
    # Test 1: Check wordlist loading
    print("\n1️⃣  Checking wordlist loading...")
    wordlist = scanner.load_wordlist()
    print(f"   ✓ Wordlist loaded: {len(wordlist)} entries")
    
    # Test 2: Check permutation generation
    print("\n2️⃣  Checking permutation generation...")
    perms = scanner.generate_permutations(wordlist[:10])
    print(f"   ✓ Permutations generated: {len(perms)} variations")
    
    # Test 3: Check check_subdomain_exists with multiple record types
    print("\n3️⃣  Testing subdomain existence check (multiple record types)...")
    test_subs = ["www", "mail", "ns1", "dns"]
    for sub in test_subs:
        full = f"{sub}.{test_domain}"
        exists = scanner.check_subdomain_exists(full)
        status = "✓ EXISTS" if exists else "✗ Not found"
        print(f"   {full:30} {status}")
    
    # Test 4: Run a mini deep scan
    print("\n4️⃣  Running deep scan (limited test)...")
    print(f"   Testing with limited candidates...")
    
    # Directly test scan_subdomain on common known subdomains
    test_list = ["www", "mail", "ns1", "smtp", "pop"]
    found = 0
    not_found = 0
    
    for sub in test_list:
        result = scanner.scan_subdomain(sub)
        if result:
            print(f"   ✓ Found: {result.subdomain} ({result.status_text})")
            found += 1
        else:
            print(f"   ✗ Not found: {sub}.{test_domain}")
            not_found += 1
    
    print(f"\n📊 Results:")
    print(f"   Found: {found}")
    print(f"   Not found: {not_found}")
    
    if found > 0:
        print("\n✅ Deep scan is now working!")
        return True
    else:
        print("\n❌ Deep scan still not finding subdomains")
        return False

if __name__ == "__main__":
    try:
        success = test_deep_scan_fix()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
