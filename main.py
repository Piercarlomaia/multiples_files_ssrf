import shutil
import os

video_extensions = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov',
                    '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv',
                    '.webm','.vcd']



audio_extensions = ['.mp3', '.wav', '.ogg', '.flac', '.mid', '.m4a','.aac','.wma',
                    '.mpa','.ra','.raw', '.aiff', '.amr', '.ape', '.au', '.dts',
                    '.dtshd', '.dvd-audio', '.eac3', '.flac', '.mka', '.m4b','.mp1',
                    '.mp2','.mpc','.mpp','.oma','.opus','.qcp','.shn','.tak','.tta',
                    '.vqf','.wv','.xm','.aac','.m3u', '.pls', '.alac', '.amr', '.ac3',
                    '.aif','.m3u','.pls']

image_extensions = ['.gif','.jpg','.jpeg','.png','.bmp','.gif','.svg','.ico',
                    '.tif','.tiff','.raw','.psd','.eps','.ai','.indd','.pdf',
                    '.webp', '.heif','.bat','.bpg', '.cd5', '.cdr','.cpt','.dcs',
                    '.dng', '.drw','.egm', '.emf','.epx','.exr', '.fpx','.hdri',
                    '.heic','.indt','.jbig', '.jng','.jp2', '.jxr','.mat','.mng',
                    '.mrw','.nef', '.orf','.pat', '.pef','.pict', '.pns','.pntg',
                    '.ptx','.pxr','.sct','.sfw', '.sgi','.targa','.wbm','.webp',
                    '.xbm','.xcf','.3fr','.ari','.arw','.srf','.sr2','.bay','.crw',
                    '.cr2', '.cap','.dcs','.dcr','.dng','.drf','.eip','.erf','.fff',
                    '.iiq','.k25','.kdc','.mdc','.mef','.mos','.nrw','.obm','.pef',
                    '.ptx','.pxn','.r3d','.raf','.raw','.rwl','.rw2','.rwz','.srw',
                    '.x3f']

extensions = image_extensions + video_extensions + audio_extensions

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
copy_and_change_extension('calculadora.m3u', extensions)