# Mask Message

**Description**

This exploit gives you the ability to mask messages (hide messages inside other messages)

**Usage**
```
$ py example.py <token> <channel id> "<displayed message>" "<hidden message>"
```

**Original author**

unknown

## Examples

**Spoofed URL**
```
$ py example.py <token> <channel id> "<https://discord.com>" "https://pornhub.com"
```

**Masked mention**
```
$ py example.py <token> <channel id> "Hello there!" "@everyone"
```

**Spoofed vanity URL**
```
$ py example.py <token> <channel id> "discord.gg/checksum" "discord.gg/2wy3ckw"
```
