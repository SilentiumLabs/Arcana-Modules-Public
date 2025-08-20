# JWT Decoder (Local)

Decodes the header and payload of a provided JWT string.  
Runs offline only — does not attempt validation, replay, or signature verification.
This is your Python script. Save it inside **`arcana-modules-public/cors-check-local/cors_check_local.py`**:

```python
#!/usr/bin/env python3
import sys, requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cors_check_local.py <port>")
        sys.exit(1)
    port = sys.argv[1]
    url = f"http://127.0.0.1:{port}/"
    try:
        r = requests.get(url, headers={"Origin": "http://example.test"})
        print(f"GET {url} status={r.status_code}")
        for k in ["Access-Control-Allow-Origin","Access-Control-Allow-Credentials"]:
            if k in r.headers:
                print(f"{k}: {r.headers[k]}")
            else:
                print(f"{k}: <absent>")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
