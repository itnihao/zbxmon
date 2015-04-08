__author__ = 'Harrison'

import zbxmon.lib.flup_fcgi_client as flup_fcgi


class PhpFpmMonitor(object):
    def __init__(self, host, port):
        self._fcgi = flup_fcgi.FCGIApp(host=host, port=port)
        self._fcgi_env = {
            'SCRIPT_FILENAME': None,
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': None,
            'REQUEST_URI': None,
            'GATEWAY_INTERFACE': 'CGI/1.1',
            'SERVER_SOFTWARE': 'zbxmon',
            'REDIRECT_STATUS': '200',
            'CONTENT_TYPE': '',
            'CONTENT_LENGTH': '0',
            # 'DOCUMENT_URI': '/uuzu-php-app_status',
            'DOCUMENT_ROOT': '/',
            'DOCUMENT_ROOT': '/var/www/',
            #'SERVER_PROTOCOL' : ???
            'REMOTE_ADDR': host,
            'REMOTE_PORT': port,
            'SERVER_ADDR': host,
            'SERVER_PORT': port,
            'SERVER_NAME': host
        }

    def get_page(self, url):
        