# Deep Subdomain Scanner - Quick Start Guide

## Overview
The Subdomain Finder has been upgraded with a powerful **Deep Scan Mode** that enables comprehensive subdomain enumeration while maintaining full backward compatibility.

## What's New?

### 🚀 Deep Scan Mode
- ✅ Scan 1000+ subdomains instead of 12
- ✅ Enable DNS brute-force with advanced wordlist
- ✅ Generate subdomain permutations (dev-api, test-dev, etc.)
- ✅ Recursive scanning for nested subdomains
- ✅ View detailed HTTP/HTTPS status codes
- ✅ Export results to file

---

## How to Use

### Basic Usage (Original - Still Works!)
1. Navigate to **Subdomain Finder**
2. Enter your domain (e.g., `example.com`)
3. Click **Find Subdomains**
4. Results appear in ~1-2 seconds

**Output**: List of found subdomains

### Advanced Usage (NEW - Deep Scan Mode)
1. Navigate to **Subdomain Finder**
2. Enter your domain (e.g., `example.com`)
3. **Enable the Deep Scan Mode toggle** 🚀
4. Click **Find Subdomains**
5. Wait 30-120 seconds for comprehensive results
6. View detailed status information
7. **(Optional)** Click Export to save results

**Output**: Detailed results with status codes and DNS information

---

## Understanding Results

### Status Codes Explained

| Status | Meaning | Example |
|--------|---------|---------|
| **200** | ✅ Live | Subdomain is active and responding |
| **301/302** | 🔄 Redirected | Subdomain redirects to another URL |
| **401/403** | 🔒 Restricted | Access denied (authentication required) |
| **Timeout** | ⏱️ Unreachable | Server not responding |
| **NXDOMAIN** | ❌ Invalid | DNS record doesn't exist |
| **WILDCARD** | 🎭 Filtered | Matches wildcard DNS (false positive) |

### Example Output
```
Subdomain                    Status Code    Status
────────────────────────────────────────────────────
api.example.com             200            Live
dev.example.com             403            Restricted
test.example.com            301            Redirected
admin.example.com           401            Restricted
staging.example.com         -              NXDOMAIN
backup.example.com          -              WILDCARD
```

---

## Feature Comparison

| Feature | Simple Mode | Deep Scan |
|---------|-------------|-----------|
| **Subdomains Checked** | 12 | 1000+ |
| **Time** | 1-2 sec | 30-120 sec |
| **DNS Brute-Force** | ❌ | ✅ |
| **Permutations** | ❌ | ✅ |
| **Recursive** | ❌ | ✅ |
| **DNS Records** | Basic | A, AAAA, CNAME, MX, TXT |
| **HTTP Status Check** | ❌ | ✅ |
| **Wildcard Detection** | ❌ | ✅ |
| **Progress Bar** | ❌ | ✅ |
| **Export Results** | ❌ | ✅ |

---

## Tips & Tricks

### When to Use Simple Mode?
- Quick reconnaissance
- Limited time available
- Just need common subdomains
- Basic domain enumeration

### When to Use Deep Scan?
- Comprehensive domain mapping
- Red team assessment
- Finding hidden subdomains
- Detailed service enumeration

### Optimizing Deep Scan
1. **Network**: Ensure good internet connection (affects DNS timeouts)
2. **Time**: Run during off-peak hours to avoid rate limiting
3. **Results**: Export and filter results locally if needed

### Common Findings
- `www` - Public web server
- `mail` - Email server
- `api` - API endpoint
- `admin` - Admin panel
- `test` / `dev` / `staging` - Development environments
- `blog` / `shop` - Content sections
- `cdn` - Content delivery network

---

## Troubleshooting

### No Subdomains Found?
- ✓ Check domain spelling
- ✓ Verify DNS is working (try simple mode first)
- ✓ Some domains may not have exposed subdomains
- ✓ Check firewall settings

### Scan Timing Out?
- ✓ Check network connection
- ✓ Reduce timeout duration in settings
- ✓ Try simple mode for initial test

### Too Many Results?
- ✓ Filter by status code
- ✓ Export and analyze separately
- ✓ Look for patterns in results

### Missing Expected Subdomain?
- ✓ May be behind WAF/proxy
- ✓ Private-only subdomain (not DNS-resolving)
- ✓ Subdomain may require special authentication

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Submit form (when domain field focused) |
| `Ctrl+C` | Cancel ongoing scan (if available) |

---

## Best Practices

### Information Gathering
1. Start with simple mode for quick assessment
2. Use deep scan for comprehensive enumeration
3. Export and organize results
4. Cross-reference with DNS records

### Security Testing
1. Always get authorization before scanning
2. Use results to identify exposed services
3. Test authentication on restricted subdomains
4. Document findings for reporting

### Performance
1. Avoid scanning during peak hours
2. Utilize export feature to save time
3. Reuse previous scan results
4. Filter results by status code

---

## Keyboard Tips

- Focus on the domain input field (auto-focus)
- Type domain name and press `Enter` to start scan
- Check toggle status before submitting
- Monitor progress bar during deep scan

---

## Advanced Features

### Export Format
Results export as **Tab-Separated Values (TSV)**:
```
Subdomain               Status Code    Status
api.example.com        200            Live
dev.example.com        403            Restricted
```

Import into Excel or your analysis tool!

### Combination Scanning
Use with other VulnX tools:
1. **Subdomain Finder** → Discover subdomains
2. **Header Analyzer** → Check security headers
3. **OSINT Recon** → Gather additional intel
4. **Network Mapper** → Map infrastructure

---

## FAQ

**Q: How long does deep scan take?**
A: Typically 30-120 seconds depending on results count and network speed.

**Q: Can I stop a scan?**
A: Refresh the page to stop the current scan (progress may be lost).

**Q: Are results saved?**
A: Results are displayed and can be exported. Use export to save permanently.

**Q: What's the maximum subdomains found?**
A: Theoretical limit is 1000+, actual depends on the domain's configuration.

**Q: Is this legal?**
A: Yes, for authorized security testing. Always get proper authorization before scanning.

**Q: How accurate are results?**
A: Very accurate for DNS resolution, wildcard detection filters false positives.

---

## Support & Documentation

For more information:
- 📖 [Full Documentation](DEEP_SUBDOMAIN_SCANNER.md)
- 🔧 [Implementation Details](DEEP_SUBDOMAIN_IMPLEMENTATION.md)
- 🧪 [Technical Specifications](src/core/deep_subdomain_scanner.py)

---

## Version Info

**Feature Release**: Deep Subdomain Scanner v1.0
**Date**: 2026-02-25
**Status**: ✅ Production Ready
**Compatibility**: ✅ Fully Backward Compatible

---

Enjoy your enhanced subdomain reconnaissance! 🎯
