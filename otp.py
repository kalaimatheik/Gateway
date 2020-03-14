import pyotp

def key():
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")       #Generates OTP scan the otp.png file using Authy or Microsoft Authenticator to get the OTP Token
    return totp.now()


print(key())                # printing it for temporarily validating the login