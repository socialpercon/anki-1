import threading
import sys
import anki_tool.rest as rest

def start_api_server(host, port, debug=False, ssl_context=None):
    for name in rest.__VIEWS__:
        __import__("anki_tool.rest.%s" % name)
    t = threading.Thread(target=rest.app.run, name='anki-rest-server-thread', kwargs={
        'host': host, 'port': port,
        'debug': debug, 'ssl_context': ssl_context
    })

    t.setDaemon(True)
    t.start()

    return t

def main(argv):
    t = start_api_server(host='0.0.0.0', port=3459,
                     debug=False)
    t.join()

if __name__ == "__main__":
    main(sys.argv[1:])

