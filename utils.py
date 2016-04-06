import os,io,zipfile
from urllib.request import urlopen

#Download Stanford Named Entity Recognizer version 3.6.0
stanford_ner_zip_url="http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip"

def download(url,data_dir,filename):
#    try:
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        web_file = urlopen(url)
        #        if 'html' in web_file.headers['content-type']:
        #            raise Exception()
        #    except:
        #        web_file = None
        if web_file is not None:
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            file = io.open(os.path.join(data_dir, filename), 'wb')
            file.write(web_file.read())
            file.close()

    name, ext = filename.rsplit('.', 1)
    if (ext == 'zip'):
        zipfile.ZipFile(os.path.join(data_dir, filename)).extractall(data_dir)


    #file_obj = io.open(os.path.join(data_dir, filename), 'r', encoding='utf-8')

download(stanford_ner_zip_url,".","stanford-ner-2015-12-09.zip")
