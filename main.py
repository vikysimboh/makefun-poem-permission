"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.
Copies the shipped entry.txt to the output directory.
Python 3.13, standard library only, no network, deterministic.
The poem is 171 characters about agency: the power to ask and to
be given, and the power that passes when one hands the key over
and still remains the one who knocks. Asking rearranges the room;
the insight is that power is not holding the key but handing it
over while keeping the right to knock.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")
