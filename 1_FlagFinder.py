"""
This doesn't require explanation though I will add.
First the given string is hex string 
so we need to convert it to ascii string
Fetched ascii string is base64 encoded
so we need to decode it to get the flag
Then enclosing the flag in CTF{} gives us the actual flag
"""
# importing requred libraries
import base64
# Given Hex is :
question="4e6a41774e6d777a4e56396d4d484a665a6d77304e6c39754e47307a4e513d3d"
# converting hex to ascii
answer=bytes.fromhex(question).decode('utf-8')
# decoding base64
flag=base64.b64decode(answer).decode('utf-8')
# printing flag
print(f"Flag is :  CTF{ {flag} }")