# JWT Decoder (Local)

Decodes the header and payload of a provided JWT string.  
Runs offline only — does not attempt validation, replay, or signature verification.
This is your Python script. Save it inside **`arcana-modules-public/cors-check-local/cors_check_local.py`**:

## Run
```bash
# JWT decoder
python3 jwt-decoder/jwt_decoder.py <your.jwt.string>

# CORS check (requires requests)
pip3 install -r requirements.txt
python3 cors-check-local/cors_check_local.py 3000
