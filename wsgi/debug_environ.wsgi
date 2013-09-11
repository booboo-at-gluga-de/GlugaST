import os

def application(environ, start_response):
    status  = '200 OK' 
    output  = 'It follows the listing of system environment variables:\n'
    output += '-------------------------------------------------------\n\n'

    for key in os.environ:
        output += "%s = %s\n" % (key, os.environ[key])

    output += '\n\n'
    output += 'It follows the listing of environ delivered by wsgi:\n'
    output += '----------------------------------------------------\n\n'

    for key in environ:
        output += "%s = %s\n" % (key, environ[key])

    output += '\n\n'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
