#!/usr/bin/env python3
"""
Debug script to trace through scan_subdomain
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.deep_subdomain_scanner import DeepSubdomainScanner

def debug_scan():
    """Debug the scanning process step by step"""
    
    domain = "google.com"
    scanner = DeepSubdomainScanner(domain, deep_scan=True)
    
    # Manually trace through scan_subdomain for "www"
    sub = "www"
    full_domain = f"{sub}.{domain}"
    
    print(f"Debugging scan_subdomain for: {full_domain}\n")
    
    print("Step 1: Check if subdomain exists")
    exists = scanner.check_subdomain_exists(full_domain)
    print(f"  Result: {exists}\n")
    
    if not exists:
        print("  ❌ check_subdomain_exists returned False, would return None")
        return
    
    print("Step 2: Get DNS records")
    dns_records = scanner.get_dns_records(full_domain)
    print(f"  DNS Records: {dns_records}\n")
    
    print("Step 3: Get A record IP")
    ip = scanner.resolve_dns(full_domain)
    print(f"  IP from A record: {ip}\n")
    
    print("Step 4: Check wildcard match")
    print(f"  wildcard_ip (from detection): {scanner.wildcard_ip}")
    if scanner.wildcard_ip and ip and ip == scanner.wildcard_ip:
        print(f"  ❌ Matches wildcard! Would return None")
        return
    else:
        print(f"  ✓ Doesn't match wildcard (or wildcard not set)\n")
    
    print("Step 5: Check HTTP status")
    status_code, status_text = scanner.check_http_status(full_domain)
    print(f"  Status Code: {status_code}")
    print(f"  Status Text: {status_text}\n")
    
    print("Step 6: Create result")
    from core.deep_subdomain_scanner import SubdomainResult
    
    result = SubdomainResult(
        subdomain=full_domain,
        status_code=status_code,
        status_text=status_text if status_text else "Found",
        dns_records=dns_records
    )
    
    print(f"  Result Object Created:")
    print(f"    - subdomain: {result.subdomain}")
    print(f"    - status_code: {result.status_code}")
    print(f"    - status_text: {result.status_text}")
    print(f"    - dns_records: {len(result.dns_records)} record types")
    print(f"\n✅ Result would be returned successfully!")
    
    # Now actually call scan_subdomain
    print("\n" + "="*60)
    print("Actually calling scan_subdomain...")
    actual_result = scanner.scan_subdomain(sub)
    
    if actual_result:
        print(f"✅ Got result: {actual_result.subdomain}")
    else:
        print(f"❌ Got None result")

if __name__ == "__main__":
    debug_scan()
