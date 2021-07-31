## Grabber
I'd recommend looking into the code before just using it straight away.

### Some things to note:
* The webhook urls are encoded in base64 for extra encryption.
* The chrome passwords are encrypted by default, I wouldn't recommend changing that, as if you accidently leaked it, you're fucked.
  - You can easily decrypt them with the key and the decrypt_pass.py file.

Chrome Passwords was from the [Backdoor Machine](https://github.com/yunusborazan/Backdoor-Machine).
