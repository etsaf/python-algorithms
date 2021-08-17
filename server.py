#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 8006

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    def _set_response(self, content_type):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()    

    #Handler for the GET requests
    def do_GET(self):
        
        path = self.path
        
        if (path == "/"):
            path = "/index.html"
        
        typ = path.split(".")[-1]
        
        if (typ == "html"):
            self._set_response("text/html")
        elif (typ == "js"):
            self._set_response("application/javascript")
        elif (typ == "css"):
            self._set_response("text/ccs")
        elif (typ == "ico"):
            return
        elif (typ == "json"):
            self._set_response("application/json")
        elif (typ == "png"):
            self._set_response("image/png")
            path = path[1:]
            fin = open(path, "rb")
            self.wfile.write(fin.read())
            fin.close()
        path = path[1:]
        fin = open(path, "r")
        self.wfile.write(bytes(fin.read(), "utf8"))
        fin.close()
        return
    
    def do_POST(self):
        path = self.path
        
        if (path == "/my-handling-form-page"):
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length).decode("utf8")  # <--- Gets the data itself
            print( "Received data:" + post_data)
            try:
                fin = open("table.json", "r")
                fin.close()
            except:
                fout = open("table.json", "w")
                fout.write("{}")
                fout.close()
            fin = open("table.json", "r")
            table = json.load(fin)
            data = json.loads(post_data)
            name = data["name"]
            if (self.is_OK(name)):
                if (name not in table):
                    table[name] = data["pts"]
                else:
                    table[name] = max(table[name], data["pts"])
            fin.close()
            fout = open("table.json", "w")
            json.dump(table, fout)
            self._set_response("")
        else:
            self.send_response(404)
            self.end_headers()    
            

    def is_OK(self, name):
        return True

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
