import pathlib

p = pathlib.path(".")
for pf in p.glob("a*"):
    if pf.is_dir():
        print(pf)
