# AnotherPcap
---
## Approach
Open pcap with Wireshark.
I try to find flag information, especially checking the path.

## Solution
You find "GET /nothinghere.tar.zip" method. Client try to download zip file. So, let's extract zip file.
in Wireshark,
1. Click File tab.
2. Select Export Objects.
3. Select HTTP.
4. Save.

You could open tar/zip file, and find flag.txt including base64 string.

## Flag
```
DawgCTF{3xtr4ct1ng_f1l35_1s_fun}
```