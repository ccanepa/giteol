from __future__ import print_function
import sys

def eol_counts(fname):
    with open(fname, "rb") as f:
        text = f.read()

    s = text.replace("\r\n", "@")
    cnt_crlf =0
    for c in s:
        if c=="@":
            cnt_crlf += 1

    cnt_lf = 0
    for c in s:
        if c=="\n":
            cnt_lf += 1

    return cnt_crlf, cnt_lf

def eol_type(fname):
    cnt_crlf, cnt_lf = eol_counts(name)
    if cnt_crlf==0:
        eol_type = "LF"
    elif cnt_lf == 0:
        eol_type = "CRLF"
    else:
        eol_type = "mixed"
    return eol_type

fnames = ["a.py",
          "b.txt",
          "c.rst",
          "d.bat",
          "e.foo",
          "f.anim",
          ]
if sys.platform.startswith("win"):
    os = "win"
else:
    os = "*nix"

print("\nOS:", os)
for name in fnames:
    print("%s: %s" % (name, eol_type(name)))
