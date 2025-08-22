# Vigenère Cipher — Encrypt & Decrypt in Python

A compact Python implementation of the classic **Vigenère cipher** with simple helpers to **encrypt** and **decrypt** text. Non-alphabet characters (spaces, punctuation, digits) are preserved, and the cipher operates on lowercase letters `a–z`.

> Example: Decrypting  
> `mrttaqrhknsw ih puggrur` with key `happycoding` → **`freecodecamp is awesome`**

---

## 🔧 What’s in the code?

- `vigenere(message, key, direction=1)`: Core function that shifts letters based on the `key`.
  - `direction=+1` → **Encrypt**
  - `direction=-1` → **Decrypt**
- `encrypt(message, key)`: Convenience wrapper for encryption.
- `decrypt(message, key)`: Convenience wrapper for decryption.

```python
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
```

---

## 🧠 How the Vigenère cipher works (quickly)

- Think of it as multiple Caesar shifts.
- Each plaintext letter is shifted by an amount determined by the **corresponding key letter**.
- The key repeats cyclically over the message.
- Decryption reverses the shift.

---

## ▶️ Usage

### Decrypt (current example in your script)
```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

print('Encrypted text:', text)
print('Key:', custom_key)

decryption = decrypt(text, custom_key)
print('Decrypted text:', decryption)
# Output: freecodecamp is awesome
```

### Encrypt
```python
plain = 'freecodecamp is awesome'
custom_key = 'happycoding'

cipher = encrypt(plain, custom_key)
print('Encrypted text:', cipher)
# Output: mrttaqrhknsw ih puggrur
```

---

## 🔁 “What do I tweak to encrypt or decrypt?”

You have **two options**:

### Option A — Use the helper functions (recommended)
- **Encrypt:** call `encrypt(message, key)`
- **Decrypt:** call `decrypt(message, key)`

```python
cipher = encrypt('your message', 'yourkey')
plain  = decrypt(cipher, 'yourkey')
```

### Option B — Call the core `vigenere` with `direction`
- **Encrypt:** `vigenere(message, key, direction=+1)` *(default)*
- **Decrypt:** `vigenere(message, key, direction=-1)`

```python
cipher = vigenere('your message', 'yourkey',  1)  # encrypt
plain  = vigenere(cipher,        'yourkey', -1)  # decrypt
```

> In short: **change `direction` to `-1` to decrypt**; use `+1` (or omit) to encrypt.

---

## ✍️ Notes & gotchas

- **Case handling:** The function converts input to **lowercase**. To preserve original case, you’d need a small enhancement.
- **Non-letters:** Characters like spaces, punctuation, digits are **kept as-is** and **do not advance** the key index.
- **Alphabet:** Only the 26 English letters are ciphered (`a–z`).
- **Security:** Vigenère is a **classical cipher**—great for learning, not for real-world security.

---

## ✅ Quick test block (optional)

```python
assert decrypt(encrypt('freecodecamp is awesome', 'happycoding'), 'happycoding') == 'freecodecamp is awesome'
assert vigenere('abc xyz', 'key', 1) == encrypt('abc xyz', 'key')
assert vigenere('mrttaqrhknsw ih puggrur', 'happycoding', -1) == 'freecodecamp is awesome'
print('All tests passed!')
```

---

## 📦 Project structure (suggested)

```
.
├── vigenere.py      # your code
└── README.md        # this file
```
