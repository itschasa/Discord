# Windows Denial of Service

**Description**

This exploit sends a URI that causes a local DoS (black screen of death) on Windows machines if interacted with. A simple system reboot will fix the DoS, so it's pretty harmless, yet fun to abuse.

**Origial founder**

[0x41.cf](https://0x41.cf/infosec/2019/05/28/skype-web-plugin-ez-rce.html)

**Usage**
```
$ py example.py <token> <channel id>
```

Click on the URI and see what happens ;))