
from flask import Flask, make_response, send_file
import sys
import os

app = Flask(__name__)

IMG_STORAGE = 'D:/Image_Storage'

@app.route("/<dir>/<filename>", methods=['POST', 'GET'])
def imagefind(dir, filename):

    imgpath = os.path.join(IMG_STORAGE, dir, filename)    
    return send_file(imgpath, mimetype='image/png')

@app.route("/<path>", methods=['POST', 'GET'])
def imagelist(path):
    
    if path == 'root':
        file_list = fileBrowser(IMG_STORAGE)
    else:
        dirpath = os.path.join(IMG_STORAGE, path)
        file_list = fileBrowser(dirpath)

    ret_str = "<p> File Lists "
    ret_str += "<DL>\n"
    for item in file_list:
        file_path = os.path.join(IMG_STORAGE, item)

        if os.path.isdir(file_path):
            a_href = "<a href='/%s'>%s</a>" % (item, item)

        else:
            img_tag = "<img src='/%s/%s'>" % (path, item)
            a_href = "<a href='/%s/%s'>%s</a>" % (path, item, img_tag)
        
        ret_str += '<li>' + a_href + '</li>\n'            
            
    return ret_str 


def fileBrowser(root_path):
    
    if not os.path.isdir(root_path):
        return 
    
    dir_paths = os.listdir(root_path)
    
    return dir_paths

if __name__ == "__main__":
    app.run()
