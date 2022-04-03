# A tale of eggs

Author: [ShadowRnG](https://github.com/ShadowRnG)

## Description

Gap in communication due to different byte ordering

## Sources

- [A briefcase](./briefcase.py)
- [chall.out](./chall.out)
- [Altered briefcase](./sol.py)

```
After buying 32 eggs from the shop, you tried to come to a decisive answer to one of life's many mysteries: should one break eggs on the little-end or the big-end? That's when you noticed a briefcase and two people who were evidently struggling to communicate with each other. Why don't you go over and see what the matter is about?
hint1: ON HOLY WARS AND A PLEA FOR PEACE
hint2: A WORD is 32 bytes
hint3: Mr.Nux I. likes to eat his eggs from the little end
```
## Exploit

There are a few ways to go about this challenge. If you choose to talk to the two people, you'll have to figure out their system of communication. All dialogues start with '0x' and this should be a clear indication that the string following '0x' is in hex. However, while Mr. Uni X's dialogues can directly be converted from hex to text, Mr. Nux I's dialogues need to be transformed first. The two of them use different byte ordering, Mr. Nux I being little endian and Mr. Uni X being big endian. For more on this, you can look up the [NUXI problem](https://nuxi.it/nuxijargon.html). If you successfully solve the challenge, you'll be rewarded with the code to the briefcase. Alternatively, you can simply [alter](./sol.py) the briefcase's code to bruteforce for the flag.

The flag is:

```
wtfCTF{u53_4_b0m_6385}
```
