# Deep Subdomain Scanner - Feature Documentation

## Overview

The Subdomain Finder module has been upgraded with a powerful "Deep Scan" mode that enables comprehensive subdomain enumeration without modifying any existing functionality or breaking current UI/logic.

## Features

### 1. **Dual Scanning Modes**

#### Simple Mode (Default - Backward Compatible)
- Uses default list of 12 common subdomains (www, mail, ftp, dev, test, etc.)
- Fast scanning (~1-2 seconds)
- No additional dependencies
- Existing functionality preserved

#### Deep Scan Mode (New)
- DNS brute-force with 1000+ wordlist entries (easily expandable to 50k+)
- Subdomain permutation logic (dev-api, test-dev, stage1, etc.)
- Recursive scanning (scans subdomains of discovered subdomains)
- Multiple DNS record types support (A, AAAA, CNAME, MX, TXT)
- Concurrent scanning with configurable thread pool (50 workers in deep mode)
- Wildcard DNS detection and filtering
- HTTP/HTTPS status code checking

### 2. **Advanced Features**

#### DNS Resolution
- Resolves subdomains to IP addresses
- Detects and filters wildcard DNS entries
- Supports both IPv4 and IPv6
- Multiple DNS record type queries

#### Status Detection
Results show detailed status information:
- **200** → Live (subdomain is active and responding)
- **301/302** → Redirected (subdomain redirects to another URL)
- **401/403** → Restricted (subdomain exists but access is restricted)
- **Timeout** → Unreachable (subdomain exists but not responding to HTTP)
- **NXDOMAIN** → Invalid (subdomain DNS record doesn't exist)
- **WILDCARD** → Filtered (matches wildcard DNS record)

#### Performance Optimization
- Concurrent HTTP requests with configurable timeouts (3-5 seconds)
- Thread pool executor for parallel DNS lookups
- Smart wildcard detection to reduce false positives
- Recursive scanning limited to relevant subdomains
- Progress tracking with percentage indicator

### 3. **User Interface Enhancements**

#### Deep Scan Toggle
A new checkbox in the UI allows users to enable/disable Deep Scan mode:
```
🚀 Deep Scan Mode [Toggle Switch]
Enable for DNS brute-force with 50k+ wordlist, permutations & recursive scanning
```

#### Results Display
Results are displayed with detailed information:
- Subdomain name
- HTTP/HTTPS status code
- Status text (Live, Restricted, Redirected, etc.)
- DNS detection status

#### Progress Indicator
While scanning, users see:
- Live percentage progress
- Number of subdomains scanned
- Current scanning message

#### Export Functionality
Results can be exported to a text file in the format:
```
Subdomain                Status Code    Status
api.example.com         200            Live
dev.example.com         403            Restricted
test.example.com        -              NXDOMAIN
```

## Usage

### Basic Usage (Simple Mode)
1. Navigate to "Subdomain Finder"
2. Enter domain name (e.g., example.com)
3. Click "Find Subdomains"
4. Results appear within 1-2 seconds

### Advanced Usage (Deep Scan Mode)
1. Navigate to "Subdomain Finder"
2. Enter domain name (e.g., example.com)
3. **Enable the "Deep Scan Mode" toggle**
4. Click "Find Subdomains"
5. Wait for comprehensive scanning (may take 30-60 seconds depending on results)
6. View detailed results with status codes
7. Optionally export results

## Technical Implementation

### Backend Architecture

#### New Module: `src/core/deep_subdomain_scanner.py`
- **DeepSubdomainScanner**: Main scanning class
  - `simple_scan()`: Basic subdomain enumeration
  - `deep_scan()`: Comprehensive scanning with all features
  - `scan()`: Unified interface that calls appropriate scan mode

- **SubdomainResult**: Data class for result representation
  - Stores subdomain, status code, status text, DNS records

#### Supporting Files
- **`data/subdomains.txt`**: Wordlist for DNS brute-force (1000+ entries, expandable)
- **Updated `src/app.py`**: Flask route handles both simple and deep modes
- **Updated `templates/subdomain.html`**: Enhanced UI with toggle and progress

### API Integration

The subdomain route accepts:
- **POST parameter**: `domain` (required) - target domain to scan
- **POST parameter**: `deep_scan` (optional) - "on" to enable deep scan mode

Response includes:
```json
[
  {
    "subdomain": "api.example.com",
    "status_code": 200,
    "status_text": "Live",
    "dns_records": {"A": ["192.168.1.1"]},
    "is_wildcard": false
  },
  ...
]
```

## Dependencies

New dependency added:
- **dnspython**: For advanced DNS queries
  - Supports multiple DNS record types
  - Better error handling for DNS failures
  - More reliable than socket-based resolution

Existing dependencies utilized:
- **requests**: For HTTP/HTTPS status checking
- **concurrent.futures**: For parallel scanning
- **threading**: For concurrent operations

## Backward Compatibility

✅ **Fully backward compatible**
- Existing `check_subdomain()` function in `scanner.py` remains unchanged
- Simple mode uses existing logic
- All other modules (sidebar, navigation, dashboard, history) unaffected
- No breaking changes to any existing functionality

## Performance Characteristics

### Simple Mode
- **Subdomains checked**: 12 (default list)
- **Time**: 1-2 seconds
- **Workers**: 10 concurrent threads
- **Best for**: Quick reconnaissance

### Deep Scan Mode
- **Subdomains checked**: 1000+ (customizable up to 50k+)
- **Time**: 30-120 seconds (varies by domain and network)
- **Workers**: 50 concurrent threads
- **Features**: Permutations, recursive scanning, detailed status
- **Best for**: Comprehensive enumeration

## Example Output

```
Subdomains found for: example.com (Deep Scan)

api.example.com          → 200  → Live
dev.example.com          → 403  → Restricted
test.example.com         → -    → NXDOMAIN
admin.example.com        → 301  → Redirected
www.example.com          → 200  → Live
```

## Security Considerations

1. **Rate Limiting**: Consider implementing rate limiting for DNS queries
2. **Timeout Handling**: All requests have 5-second timeout to prevent hanging
3. **Wildcard Detection**: Automatically filters false positives from wildcard DNS
4. **Recursive Limits**: Recursive scanning limited to prevent infinite loops
5. **Thread Safety**: ThreadPoolExecutor ensures thread-safe operations

## Future Enhancements

Potential improvements for future versions:
- DNS query timeout optimization per domain
- Support for custom word lists upload
- Saved scan history with comparison
- Integration with authentication detection
- SSL certificate enumeration
- Service version detection
- 3rd-party API integration (Shodan, AlienVault, etc.)

## Troubleshooting

### No subdomains found in deep scan
- Check DNS connectivity
- Verify domain name is correct
- Some domains may not have many subdomains

### Scan timing out
- Network may be slow
- Try simple mode first
- Check firewall rules

### Import errors for dnspython
- Install: `pip install dnspython`
- Verify requirements.txt is up to date

## Testing

Run integration tests:
```bash
python test_deep_subdomain_integration.py
```

All 6 test categories should pass:
- ✅ Imports
- ✅ Existing Functionality (Backward Compatibility)
- ✅ Scanner Initialization
- ✅ Wordlist Loading
- ✅ Permutation Generation
- ✅ Output Format
