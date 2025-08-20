#!/usr/bin/env python3
import base64, json, sys

def b64url_decode(s: str) -> bytes:
    s += '=' * (-len(s) % 4)
    return base64.urlsafe_b64decode(s.encode())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 jwt_decoder.py <JWT>")
        sys.exit(1)
    token = sys.argv[1]
    parts = token.split('.')
    if len(parts) < 2:
        print("Invalid JWT format")
        sys.exit(1)
    header = json.loads(b64url_decode(parts[0]))
    payload = json.loads(b64url_decode(parts[1]))
    print("== Header ==")
    print(json.dumps(header, indent=2))
    print("\n== Payload ==")
    print(json.dumps(payload, indent=2))
    if len(parts) == 3:
        print("\n== Signature (base64url) ==")
        print(parts[2])

if __name__ == "__main__":
    main()

