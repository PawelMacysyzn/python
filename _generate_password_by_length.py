import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

def main():
    print(generate_password(8))

if __name__ == '__main__':
    main()

