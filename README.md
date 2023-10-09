# Multiples Files SSRF

This script is designed to test how a server handles m3u files. It creates an m3u file in various video, image, and audio extensions to test for SSRF (Server-Side Request Forgery) bypass.

## Usage

1. Clone this repository.
2. Modify the `Calculadora.m3u` file in order to support your server. Make the necessary changes to ensure compatibility.
3. Run the script and observe how your server handles the different m3u files.

Please note that this script should be used for testing purposes only and with proper authorization. Unauthorized use is strictly prohibited.

## Supported Extensions

The script supports the following file extensions:

- Video: ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov',
                    '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv',
                    '.webm','.vcd']
- Image: ['.gif','.jpg','.jpeg','.png','.bmp','.gif','.svg','.ico',
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
- Audio: ['.mp3', '.wav', '.ogg', '.flac', '.mid', '.m4a','.aac','.wma',
                    '.mpa','.ra','.raw', '.aiff', '.amr', '.ape', '.au', '.dts',
                    '.dtshd', '.dvd-audio', '.eac3', '.flac', '.mka', '.m4b','.mp1',
                    '.mp2','.mpc','.mpp','.oma','.opus','.qcp','.shn','.tak','.tta',
                    '.vqf','.wv','.xm','.aac','.m3u', '.pls', '.alac', '.amr', '.ac3',
                    '.aif','.m3u','.pls']

Feel free to modify the script and add more extensions as required.

## Disclaimer

The author of this script is not responsible for any unauthorized or malicious use. Use this script responsibly and adhere to your local laws and regulations.
