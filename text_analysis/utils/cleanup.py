import os
import glob

def clean_outputs(directory='outputs'):
    files = glob.glob(os.path.join(directory, '*'))
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {e.strerror} - {e.filename}")
