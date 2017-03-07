from __future__ import print_function

line_lf = "aaa bbb ccc\n"
line_crlf = "xxx yyy zzz\r\n"

text = ( line_lf +
         line_crlf +
         line_lf +
         line_crlf +
         line_lf +
         line_crlf +
         line_lf
         )

fnames = ["a.py",
          "b.txt",
          "c.rst",
          "d.bat",
          "e.foo",
          "f.anim",
          ]

for name in fnames:
    with open(name, "wb") as f:
        f.write(text)

print("***done writing files***")










