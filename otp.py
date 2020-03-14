import pyotp

def key():
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    return totp.now()


print(key())