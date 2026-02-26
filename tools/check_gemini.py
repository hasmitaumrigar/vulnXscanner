#!/usr/bin/env python3
"""
tools/check_gemini.py

Simple script to validate GEMINI_API_KEY and perform a minimal request
against the Google Generative Language `generateContent` endpoint.

Usage:
  python3 tools/check_gemini.py

This script loads environment variables from a local .env file (if present).
It will NOT print the API key. It prints structured JSON about the response.
"""
import os
import sys
import json
import traceback
from dotenv import load_dotenv
import requests


def extract_text(obj):
    if not obj:
        return ''
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        for key in ('content', 'text', 'output', 'candidates', 'response'):
            if key in obj:
                val = obj[key]
                if isinstance(val, list) and val:
                    parts = [extract_text(v) for v in val]
                    return ' '.join([p for p in parts if p])
                if isinstance(val, dict):
                    return extract_text(val)
                if isinstance(val, str):
                    return val
        for v in obj.values():
            t = extract_text(v)
            if t:
                return t
    if isinstance(obj, list):
        for item in obj:
            t = extract_text(item)
            if t:
                return t
    return ''


def main():
    load_dotenv()
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        print(json.dumps({'success': False, 'error': 'Gemini API key not configured (GEMINI_API_KEY missing)'}))
        return 2

    model = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
    headers = {'Content-Type': 'application/json'}
    params = {'key': key}

    # Heuristic: if looks like OAuth access token, use as Bearer
    if isinstance(key, str) and (key.startswith('ya29.') or key.lower().startswith('bearer ')):
        token = key
        if token.lower().startswith('bearer '):
            token = token.split(' ', 1)[1]
        headers['Authorization'] = f'Bearer {token}'

    payload = {
        'contents': [
            {
                'parts': [
                    {'text': 'Ping from vulnXscanner - please respond with a short acknowledgement.'}
                ]
            }
        ]
    }

    timeout_seconds = 12

    try:
        print('Sending request to Gemini endpoint...')
        resp = requests.post(url, headers=headers, params=params, json=payload, timeout=timeout_seconds)
        status = resp.status_code
        print('HTTP status:', status)

        try:
            body = resp.json()
        except Exception:
            body = resp.text

        # If failure, print structured info
        if status == 401:
            print(json.dumps({'success': False, 'status': status, 'error': 'Unauthorized. Check GEMINI_API_KEY type (API key vs OAuth token).', 'body': body}, default=str, indent=2))
            return 3
        if status == 429:
            print(json.dumps({'success': False, 'status': status, 'error': 'Rate limited (429).'}, indent=2))
            return 4
        if status >= 400:
            print(json.dumps({'success': False, 'status': status, 'error': 'Gemini API returned error', 'body': body}, default=str, indent=2))
            return 5

        # Attempt to extract generated text
        text = extract_text(body)
        if not text:
            # fallback: pretty-print body
            print(json.dumps({'success': True, 'status': status, 'warning': 'No textual output found, full response returned', 'body': body}, default=str, indent=2))
        else:
            print(json.dumps({'success': True, 'status': status, 'analysis_text': text}, indent=2))
        return 0

    except requests.Timeout:
        print(json.dumps({'success': False, 'error': 'Request timed out'}))
        return 6
    except requests.RequestException as e:
        print(json.dumps({'success': False, 'error': 'Network error', 'detail': str(e)}))
        print(traceback.format_exc())
        return 7
    except Exception as e:
        print(json.dumps({'success': False, 'error': 'Unexpected error', 'detail': str(e)}))
        print(traceback.format_exc())
        return 8


if __name__ == '__main__':
    sys.exit(main())
