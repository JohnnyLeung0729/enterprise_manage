import hashlib

salt = b'@ZT\x03\xfc\xbc\x17\xd3=$\n\xb0\x0c\x1a_\x0c'


def crypt(mm):
    hashmm = hashlib.pbkdf2_hmac('sha512', bytes(mm, encoding='utf-8'), salt, 100000)
    return hashmm
