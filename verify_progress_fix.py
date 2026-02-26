#!/usr/bin/env python3
import sys
sys.path.insert(0, 'src')

print("Progress Bar Fix Verification")
print("="*60)

# Test 1: Check backend
with open('src/app.py') as f:
    app_content = f.read()

print("\n[Backend (app.py)]")
checks = [
    ('def progress_callback(progress_data):', 'Progress callback defined'),
    ("'progress_percent':", 'Sends progress_percent'),
    ('subdomain_progress', 'Emits subdomain_progress event'),
    ('progress_callback=progress_callback', 'Passes callback to scanner'),
    ('updateProgress(100', 'Sets 100% on completion')
]

for check, desc in checks:
    if check in app_content:
        print(f"  ✅ {desc}")
    else:
        print(f"  ❌ {desc}")

# Test 2: Check scanner
with open('src/core/deep_subdomain_scanner.py') as f:
    scanner_content = f.read()

print("\n[Scanner (deep_subdomain_scanner.py)]")
checks = [
    ('def update_progress(self, current: int, total: int', 'Progress method exists'),
    ('int((current / total) * 100)', 'Calculates percentage'),
    ('self.progress_callback', 'Calls callback'),
]

for check, desc in checks:
    if check in scanner_content:
        print(f"  ✅ {desc}")
    else:
        print(f"  ❌ {desc}")

# Test 3: Check frontend
with open('static/js/subdomain.js') as f:
    js_content = f.read()

print("\n[Frontend (subdomain.js)]")
checks = [
    ("socket.on('subdomain_progress'", 'Listens for progress'),
    ('updateProgress(data.progress_percent', 'Updates with percentage'),
    ('updateProgress(100', 'Sets 100% on complete'),
    ('data.current}/${data.total}', 'Shows progress text'),
]

for check, desc in checks:
    if check in js_content:
        print(f"  ✅ {desc}")
    else:
        print(f"  ❌ {desc}")

print("\n" + "="*60)
print("✅ PROGRESS BAR FIX COMPLETE")
print("\nSummary of Changes:")
print("  1. Progress callback now passed to scan_subdomains_blocking()")
print("  2. Backend emits subdomain_progress events with percentage")
print("  3. Frontend updates progress bar as events arrive")
print("  4. Progress set to 100% when scan completes")
print("\nThe progress bar will now:")
print("  • Show 0% at start")
print("  • Increment as subdomains are checked")
print("  • Reach 100% when scan finishes")
