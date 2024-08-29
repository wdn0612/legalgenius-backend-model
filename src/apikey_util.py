import os
import secrets
import hashlib


def generate_api_key():
    # Generate a random secret key
    random_bytes = secrets.token_bytes(32)

    # Use SHA-256 to hash the random bytes
    api_key = hashlib.sha256(random_bytes).hexdigest()

    # Optionally, prefix with a name or purpose
    api_key_name = f"LegalGeniusAPP_{secrets.token_hex(8)}"

    return api_key_name, api_key


def main():
    api_key_name, api_key = generate_api_key()

    # Print or store the generated keys
    print(f"API Key Name: {api_key_name}")
    print(f"API Key: {api_key}")

    # Optionally, you could save this to a file or database
    # with open('api_keys.txt', 'a') as f:
    #     f.write(f"{api_key_name}: {api_key}\n")


if __name__ == "__main__":
    main()
