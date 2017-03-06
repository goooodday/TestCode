## Image Browser on the Flask!

Based on the Flask, you can browse images of the local path on the Web.

### File Info 
* ImageBrowser.py : Provides web services using Flask and Websocket.io.
* ImageViewer.html : HTML template file that composes the Image Browser web page
* ImageViewer.js : Java Script file for dynamic execution of Image Browser


### Configuration
For actual configuration, you need to put * .js in the static folder and * .html file in the template folder.
In addition, Bootstrap, Socket.io, and JQuery files should be placed in the static folder.

### File Tree

```
-- /
   |-- ImageBrowser.py
   |-- static
   |     |- ImageViewer.js
   |     |- other *.js(bootstrap, socket.io, jquery)
   |-- templates
         |- ImageViewer.html
```
