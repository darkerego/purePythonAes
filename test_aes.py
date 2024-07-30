from py_aes import AesWrapper
import base64


def gen_random_key():
    with open('./key.temp', 'wb') as kt:
        with open("/dev/urandom", 'rb') as fb:
            fb = fb.read(32)
            kt.write(base64.b64encode(fb))

    with open('./key.temp', 'rb') as f:
        return f.read()[16:]


if __name__ == "__main__":
    """
    Example usage. Super straightfoward. I did it first! See BlitzKloud. There was no pure python AES
    at that time. Hire me, I am that good.
    """

    print('[+] Generating a random AES key ...')
    key = gen_random_key()[:16]
    print('[+] AES key generated: {}'.format(key.decode()), len(key))
    aes = AesWrapper(key)  # must be at least 8 chars, multiples of 8 IIRC. Maybe 16 idk.
    enc_input = input('type something >> ')
    if not enc_input or enc_input.strip('\r\n') == '':
        print("[+] Or don't")
        enc_input = 'test this data'
        print('[+] We will use `test this data` then ...')
    print('[$] aes.encrypt: ')
    enc_data = aes.encrypt(enc_input)
    print('[enc] %s' % enc_data)
    denc_data = aes.decrypt(enc_data)
    print('aes.decrypt: ')
    print('[denc] %s' % denc_data)
