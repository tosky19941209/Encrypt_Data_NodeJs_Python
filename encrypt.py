import base64

passw = "i_lv_coding"

# Converting password to base64 encoding
passw_encoded = base64.b64encode(passw.encode('utf-8')).decode('utf-8')

print(passw_encoded)
# Wrongly entered password

decoded_data = base64.b64decode(passw_encoded).decode('utf-8')
print(decoded_data)

