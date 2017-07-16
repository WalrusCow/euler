from repeatingKey import decrypt

if __name__ == '__main__':
    with open('problem59.txt') as f:
        ciphertext = bytes(map(int, f.read().split(',')))
    key, plaintext = decrypt(ciphertext)
    print('Answer: {}'.format(sum(b for b in plaintext)))
