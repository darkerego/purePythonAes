try:
    import PurePyAES.aes
except ImportError:
    raise ImportError("Please install PurePyAES first.")


def gen_random_key():
    with open('./key.temp', 'wb') as kt:
        with open("/dev/urandom", 'rb') as fb:
            fb = fb.read(32)
            return fb.hex().__str__()


if __name__ == "__main__":
    """
    Example usage. Super straightfoward. I did it first! See BlitzKloud. There was no pure python AES
    at that time. Hire me, I am that good.
    """

    print('[+] Generating a random AES key ...')
    key = gen_random_key()[:32]
    print('[+] AES key generated: {}'.format(key), len(key))
    aes = PurePyAES.aes.AesWrapper(key.encode())
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
