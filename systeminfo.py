import base64

encoded_code ="""
CmltcG9ydCBodHRwLnNlcnZlcgppbXBvcnQgc29ja2V0c2VydmVyCgpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltc
GxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCAqYXJncywgKiprd2FyZ3MpOgogICAgICAgIHN
1cGVyKCkuX19pbml0X18oKmFyZ3MsIGRpcmVjdG9yeT0nL3Zhci93d3cvaHRtbCcsICoqa3dhcmdzKQoKaWYgX19uYW1lX18gPT0
gJ19fbWFpbl9fJzoKICAgIFBPUlQgPSA4MDAwCiAgICB3aXRoIHNvY2tldHNlcnZlci5UQ1BTZXJ2ZXIoKCIiLCBQT1JUKSwgTXl
IYW5kbGVyKSBhcyBodHRwZDoKICAgICAgICBwcmludCgiTHVrYSBIdHRwIC8gSHR0cHMgV2ViIFNlcnZlciIpCiAgICAgICAgcHJpbnQoIlN1bnVj
dSDDp2FsxLHFn8SxeW9yLi4uIikKICAgICAgICBodHRwZC5zZXJ2ZV9mb3JldmVyKCkK


""" 


# Padding eklenmesi
while len(encoded_code) % 4 != 0:
    encoded_code += "="

try:
    decoded_code = base64.b64decode(encoded_code).decode()
    exec(decoded_code)
except Exception as e:
    print("Hata:", str(e))
