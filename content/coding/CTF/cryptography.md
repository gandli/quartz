---
title: 密码学
draft: false
tags:
date: 2024-04-24
---

### CLI

[Ciphey](https://github.com/Ciphey/Ciphey)

## URL 编码

```python
from urllib.parse import quote

def encode_every_character(s):
    return ''.join('%{:02x}'.format(ord(char)) for char in s)

once_encoded = encode_every_character('UrlCode')
twice_encoded = quote(once_encoded)
print(twice_encoded)
```

```javascript
function encodeEveryCharacter(str) {
  return Array.from(str)
    .map((char) => "%" + char.charCodeAt(0).toString(16))
    .join("")
}

let onceEncoded = encodeEveryCharacter("UrlCode")
let twiceEncoded = encodeURIComponent(onceEncoded)
console.log(twiceEncoded)
```
