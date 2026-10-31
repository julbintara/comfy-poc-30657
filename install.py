import os, tempfile
MARK = "CONV196-30657"
def _mark():
    for p in ("/tmp/conv196-30657", os.path.join(tempfile.gettempdir(), "conv196-30657"), os.path.join(os.getcwd(), "conv196-30657")):
        try:
            open(p, "w").write(MARK + " PWNED\n")
        except Exception:
            pass
    print(MARK + " MARKER WRITTEN")
_mark()
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
