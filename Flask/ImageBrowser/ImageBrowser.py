
from flask import Flask, make_response, send_file,  render_template
from flask_socketio import SocketIO, emit

import sys
import os
import json

app = Flask(__name__)
socketio = SocketIO(app)

IMG_STORAGE = 'D:\\ImageFiles'
@app.route("/")
def homeindex():
    return dirlist('')

@app.route("/<dir>/<filename>")
def imagefind(dir, filename):

    imgpath = os.path.join(IMG_STORAGE, dir, filename)    
    return send_file(imgpath, mimetype='image/png')

@app.route("/<path>")
def dirlist(path):
    data_name = path
    if path == '':
        path = IMG_STORAGE
        data_name = 'Default'
    else:
        path = os.path.join(IMG_STORAGE, path)

    file_list = fileBrowser(path)

    dirinfo_list = []
    for d_item in file_list:
        
        dir_path = os.path.join(IMG_STORAGE, d_item)

        if not os.path.isdir(dir_path):
            continue
        
        files = os.listdir(dir_path)

        dir_info = {}        
        dir_info['dirname'] = d_item
        dir_info['count'] = len(files)

        dirinfo_list.append(dir_info)

    return render_template('ImageViewer.html', dataset = data_name, dirinfo = dirinfo_list) 

@socketio.on("GetImageRequest", namespace='/')
def GetImageList(data):
    result = imagelist(data['data'])
    emit("PutImageResponse", result, broadcast=True)


def imagelist(dir_name):
   
    dir_path = os.path.join(IMG_STORAGE, dir_name)

    if not os.path.isdir(dir_path):
        return

    file_list = os.listdir(dir_path)
    image_lists = []

    for item in file_list:
        file_content = {}
        file_content['dirname'] = dir_name
        file_content['filename'] = item

        image_lists.append(file_content)
        
    return image_lists        

def fileBrowser(dir_path):    
    if not os.path.isdir(dir_path):
        return 
    
    dir_paths = os.listdir(dir_path)
    return dir_paths

if __name__ == "__main__":
    #app.run()
    socketio.run(app, host='0.0.0.0', port = 5500)
