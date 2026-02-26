#!/usr/bin/env python3
"""
tools/check_gemini_sdk.py

Try calling the new `google.genai` SDK to list models and/or generate a short response.
"""
import os, sys, json, traceback
from dotenv import load_dotenv
load_dotenv()
try:
    from google import genai
except Exception as e:
    print(json.dumps({'success': False, 'error': 'google.genai import failed', 'detail': str(e)}))
    sys.exit(2)

key = os.getenv('GEMINI_API_KEY')
if not key:
    print(json.dumps({'success': False, 'error': 'GEMINI_API_KEY missing'}))
    sys.exit(3)

try:
    client = genai.Client(api_key=key)
except Exception as e:
    print(json.dumps({'success': False, 'error': 'failed to init genai.Client', 'detail': str(e)}))
    print(traceback.format_exc())
    sys.exit(4)

# Try list models if available
try:
    # Some SDK versions expose a 'list' or 'list_models' method; try common names
    models = None
    if hasattr(client.models, 'list'):
        models = client.models.list()
    elif hasattr(client.models, 'list_models'):
        models = client.models.list_models()
    else:
        models = None
    print('models_call_result_exists:', models is not None)
except Exception as e:
    print(json.dumps({'success': False, 'action': 'list_models', 'error': str(e)}))

# Try generate_content via SDK
try:
    model = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
    resp = client.models.generate_content(model=model, contents=[{'parts':[{'text':'SDK test - please reply briefly'}]}])
    # Try to convert response to JSON-like
    try:
        if hasattr(resp, 'to_dict'):
            out = resp.to_dict()
        else:
            out = json.loads(json.dumps(resp, default=lambda o: getattr(o, '__dict__', str(o))))
    except Exception:
        out = str(resp)
    print(json.dumps({'success': True, 'status': 'ok', 'response_preview': out}, default=str) )
except Exception as e:
    print(json.dumps({'success': False, 'action': 'generate_content', 'error': str(e)}))
    print(traceback.format_exc())
    sys.exit(5)
