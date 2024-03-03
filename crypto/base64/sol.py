import base64

ct = 'bmV4dXN7YzBOZ1I0VCRfZm9yX2QzQ29kSW5HX3RIMSR9Cg==```'

print(base64.b64decode(ct).decode())

