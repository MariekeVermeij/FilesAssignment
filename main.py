__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os,glob,zipfile,shutil


def clean_cache():
    try:
        os.mkdir('files\\cache')
    except:
        try:
            os.rmdir('files\\cache')
        except:
            shutil.rmtree(('files\\cache'))  
        os.mkdir('files\\cache')

clean_cache()


def cache_zip(zip_file_path:str,cache_dir_path:str):

    with zipfile.ZipFile((zip_file_path),'r') as zip_something:
        zip_something.extractall(cache_dir_path)

cache_zip('files\\data.zip','files\\cache')


def cached_files():
    folder = os.path.abspath('files\\cache/*')
    content = glob.glob(folder)
    return content

print(cached_files())


def find_password(cached_files_list): 
    for f in cached_files_list:
        content_file = open(f,'r')
        text = content_file.readlines()
        if 'password' in str(text):
            for t in text:
                if 'password' in t:
                    return (str(t)).replace('password: ','')

print(find_password(cached_files()))