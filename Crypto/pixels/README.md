# Challenge Name

Author: [OrkinKing](https://github.com/nithinchowdary007)

## Description

My friend challenged me to obtain the secret message from the image he sent. He mentioned that image is encrypted with a special code and key. However he forgot the shifting method used to encrypt key. Key is aVLgBTOR. The word "wtfctf" might be of any help.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [encrypt.py](./encrypt.py)
- [enc.png](./enc.png)


```
My friend challenged me to obtain the secret message from the image he sent. He mentioned that image is encrypted with a special code and key. 
However he forgot the shifting method used to encrypt key. Key(encrypted) is aVLgBTOR. 
The word "wtfctf" might be of any help.
```

## Exploit

- [decrypt.py](./decrypt.py)

The flag is:

```
WTFCTF{Y0U_F0UND_M3_<3}
```