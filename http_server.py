#!/usr/bin/env python
import http.server
import socketserver
import os
import scan_package


port = int(os.environ['HELM_REPO_PORT'])
repo_url = os.environ['HELM_REPO_URL'] + ':' + (os.environ['HELM_REPO_PORT'])
web_data_dir = '/wwwdata'

def main():
    # re-generation helm repo index
    scan_package.generate_index(web_data_dir, repo_url)
    
    web_dir = os.path.join(os.path.dirname(__file__), web_data_dir)
    os.chdir(web_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("serving at port", port)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
