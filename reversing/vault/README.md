# Vault

Author: [ShadowRnG](https://github.com/ShadowRnG)

## Description

We've finally found the hideout of the infamous thief responsible for multiple break-ins and forced entries in the locality. He's stashed all things he's ever stolen behind a vault. However, we don't know the password and the only one around seems to be his pet bot.

## Sources

- [bot](./bot)
- [vault.gpg](./vault.gpg)


```
We've finally found the hideout of the infamous thief responsible for multiple break-ins and forced entries in the locality. He's stashed all things he's ever stolen behind a vault. However, we don't know the password and the only one around seems to be his pet bot.
Hint 1: Why not list out all the possible passwords?
Hint 2: Try and force your way in with the list of words
```

## Exploit

After running the [bot](./bot) a few times, it becomes evident that the passwords are always 3-lettered. Using this information, you can create a wordlist of all the possible combinations. With the help of a wordlist, you can either write a script to brute force the gpg key or use John the Ripper (first gpg2john and then crack the hash).
- [List out all passwords](./lis.py)
- [Wordlist](./wl.txt)

The flag is:

```
wtfCTF{f0rc1n8_y0ur_w4y_1n_495}
```
