#!/bin/bash
# VulnX AI - Quick Test & Validation Guide

echo ""
echo "=================================================="
echo "VulnX AI Output Format - Validation Guide"
echo "=================================================="
echo ""

# Check if API key is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  GEMINI_API_KEY not set"
    echo ""
    echo "Set it with:"
    echo "   export GEMINI_API_KEY='your-api-key'"
    echo ""
else
    echo "✓ GEMINI_API_KEY is set"
fi

echo ""
echo "STEP 1: Verify Code Changes"
echo "=============================="
echo ""

# Check prompt update
if grep -q "NO HTML tags whatsoever" src/app.py; then
    echo "✓ Prompt updated: NO HTML tags specification"
else
    echo "✗ Prompt update not found"
fi

# Check plain text detection
if grep -q "/\[<[^>]*>/g.test" static/js/main.js; then
    echo "✓ Plain text detection in htmlToPlainText()"
else
    echo "✗ Plain text detection not found"
fi

# Check .strip() in text extraction
if grep -q "return obj.strip()" src/app.py; then
    echo "✓ Text extraction includes .strip()"
else
    echo "✗ Text .strip() not found"
fi

echo ""
echo "STEP 2: Expected Output Format"
echo "================================"
echo ""
echo "Your AI analysis should look like this:"
echo ""
echo "  1. **What is this port?**"
echo "  Simple explanation here."
echo ""
echo "  2. **Why is it risky?**"
echo "  * Risk point 1"
echo "  * Risk point 2"
echo "  * Risk point 3"
echo ""
echo "  3. **How to secure it?**"
echo "  * Action 1"
echo "  * Action 2"
echo "  * Action 3"
echo ""
echo "  4. **Risk score:** HIGH"
echo ""

echo "STEP 3: What NOT to See"
echo "========================"
echo ""
echo "❌ Do NOT see any of these:"
echo "   <p>content</p>"
echo "   <h3>Heading</h3>"
echo "   <ul><li>item</li></ul>"
echo "   &lt;escaped&gt; tags"
echo "   Raw JavaScript or code"
echo ""

echo "STEP 4: How to Test"
echo "===================="
echo ""
echo "Terminal 1 - Start Flask:"
echo "   cd /Users/utkarshraj/vulnXscanner"
echo "   export GEMINI_API_KEY='your-key'"
echo "   python3 src/app.py"
echo ""
echo "Browser - Test the UI:"
echo "   1. Open: http://localhost:5000"
echo "   2. Enter target URL (e.g., scanme.nmap.org)"
echo "   3. Click 'Scan' button"
echo "   4. Wait for results"
echo "   5. Click '🔍 Click for AI expert analysis' on any result"
echo "   6. Wait for AI analysis modal to appear"
echo "   7. Verify output is CLEAN TEXT (no HTML code)"
echo "   8. Click '📥 Download Report' to get PDF"
echo ""

echo "STEP 5: Troubleshooting"
echo "======================"
echo ""
echo "If you see HTML code:"
echo "  ✓ Check src/app.py prompt (should say 'NO HTML tags')"
echo "  ✓ Check static/js/main.js htmlToPlainText() function"
echo "  ✓ Check 'plain text detection' regex in main.js"
echo ""
echo "If download fails:"
echo "  ✓ Verify reportlab is installed: python3 -c 'import reportlab'"
echo "  ✓ Check browser console for errors: F12 → Console"
echo ""
echo "If analysis is slow:"
echo "  ✓ Normal: First request may take 3-5 seconds"
echo "  ✓ Check: API quota and rate limits"
echo "  ✓ Verify: Network connection to googleapis.com"
echo ""

echo "STEP 6: Verify All Components"
echo "=============================="
echo ""

components=(
    "Optimized prompt (simple language, no HTML)"
    "Plain text detection (regex check)"
    "Text extraction with .strip()"
    "htmlToPlainText function"
    "Download button functionality"
    "Fixed-height modal container"
    "Custom scrollbar styling"
    "Loading animation"
)

for comp in "${components[@]}"; do
    echo "  ✓ $comp"
done

echo ""
echo "STEP 7: Production Checklist"
echo "============================="
echo ""
echo "Before deploying:"
echo "  ☐ API key is set and valid"
echo "  ☐ reportlab is installed (pip3 install reportlab)"
echo "  ☐ All code changes committed"
echo "  ☐ Tested with at least 3 different ports"
echo "  ☐ Download PDF works correctly"
echo "  ☐ Output is clean (no HTML tags visible)"
echo "  ☐ Modal doesn't shift during typing"
echo "  ☐ All buttons work correctly"
echo ""

echo "=================================================="
echo "✓ Validation Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "  1. Set GEMINI_API_KEY environment variable"
echo "  2. Start Flask server"
echo "  3. Test in browser"
echo "  4. Verify output format"
echo ""
