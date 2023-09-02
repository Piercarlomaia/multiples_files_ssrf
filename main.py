import shutil
import os

# create list with all known video and audio file extensions
extensions = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov',
              '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', 
              '.webm', '.vcd', '.mp3', '.wav', '.ogg', '.flac', 
              '.mid', '.m4a','.aac','.wma','.mpa','.ra','.raw', 
              '.amr', '.ac3', '.aif', '.m3u', '.pls']

# function to copy and change file extension
def copy_and_change_extension(filename, extensions):
    base, original_ext = os.path.splitext(filename)
    print(base, original_ext)
    for ext in extensions:
        if ext.lower() == original_ext.lower():
            continue
        copy_filename = base + ext
        shutil.copy(filename, copy_filename)

# usage
copy_and_change_extension('teste.wav', extensions)