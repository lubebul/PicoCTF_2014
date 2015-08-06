# Snapcat
用[Bless Hex Editor](http://home.gna.org/bless/)打開[disk image](disk.img)
 1. 我們可以用開頭的 [file signature](http://en.wikipedia.org/wiki/List_of_file_signatures) 知道檔案類型，然後抓出完整的檔案來察看。
 找到的開頭有：
  * 55AAF8...F0FF：??
  * F8FF...F0FF：??
  * 4170...4503：??
  * FFD8FFE0...FFD9：JPEG
 2. 把FFD8到FFD9的hex部份複製下來，貼到新的hex文件中，命名成jpg檔，然後就能用image viewer開啟了，第2張抓出的圖：
 ![image](flag_snapcat.jpg)
