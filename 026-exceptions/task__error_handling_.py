import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
    """
    * url (str) - http://
    * file_path (str) - location on the computer
    """
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print('Remove {}...'.format(tmpfile_path))
        os.remove(tmpfile_path)

    print('Save url: [{}] to file: [{}]'.format(url, file_path))
    save_url_to_file(url, file_path)

    print('Copy file: [{}] to [{}]'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)
    
except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('SUCCESS') 

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)

'''
Save url: [http://www.mobilo24.eu/spis/] to file: [c:/temp/spis.html]
Copy file: [c:/temp/download.tmp] to [c:/temp/spis.html]
Error downloading the URL http://www.mobilo24.eu/spis/
Error details: [Errno 2] No such file or directory: 'c:/temp/download.tmp'
'''