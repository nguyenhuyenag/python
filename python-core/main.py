import os
import pathlib

desktop = pathlib.Path.home() / 'Desktop'

# desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

print(desktop)