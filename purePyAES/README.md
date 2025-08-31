# What?

<p> The original zero dependency python only AES 
implemntation. See 
  
  [blitzkloud](https://github.com/darkerego/blitzkloud) </p>

<p>
tips ethercrypt.eth
</p>



## Example Usage

<pre>
import pureaes.py_aes


def gen_random_key():
    with open('./key.temp', 'wb') as kt:
        with open("/dev/urandom", 'rb') as fb:
            fb = fb.read(32)
            return fb.hex().__str__()


if __name__ == "__main__":
    """
    Example usage.
    """

    print('[+] Generating a random AES key ...')
    key = gen_random_key()[:32]
    print('[+] AES key generated: {}'.format(key), len(key))
    aes = pureaes.py_aes.AesWrapper(key.encode())  # must be at least 8 chars, multiples of 8 IIRC. Maybe 16 idk.
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


</pre>