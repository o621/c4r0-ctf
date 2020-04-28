# Catography

## Challenge
Jubie's released her own collection of cat pictures. Go check it out!

http://challs.houseplant.riceteacatpanda.wtf:30002

Note: The Unsplash author credit is not a part of the challenge, it's only there to conform with the Unsplash image license.

Dev: jammy

## Approach
I have tried several methods. And I found out using GPS info.

## Solution
You should download all cats image file and check GPS information.
I used exiftool and extracted GPS information to csv file.
```
exiftool -csv -GPSLongitude -GPSLatitude -n  *.jpg >exif.csv
```
Next, I used QGIS and throw csv file in that.

## Flag
```
rtcp{4round_7h3_w0r1d}
```