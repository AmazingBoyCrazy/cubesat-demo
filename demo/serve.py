#!/usr/bin/env python3
"""演示用静态服务器：强制关闭缓存。

开发中反复改代码时，浏览器缓存会导致"改了却看到旧画面"。
用法： python serve.py [端口]     默认 8123
"""
import sys, os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('serving %s  ->  http://127.0.0.1:%d/   (no-cache)' % (os.getcwd(), port))
    ThreadingHTTPServer(('127.0.0.1', port), NoCacheHandler).serve_forever()
