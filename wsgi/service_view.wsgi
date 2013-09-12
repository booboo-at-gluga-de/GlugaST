import sys, time
sys.path.append("/var/websites/lib/")
import datastore

def application(environ, start_response):
    status = '200 OK' 

    output = 'Hello World!\n'
    open_orders = datastore.get_orders( {"status": [0]} )
    for row in open_orders:
	output += "%s will %s %s (bestellt um %s), ID=%s, status=%s (%s)\n" % (row[1], row[3], row[2], time.strftime("%H:%M Uhr am %d.%m.%Y", time.localtime(row[5])), row[0], row[4], datastore.get_status(row[4]))

    output = output.encode('utf-8')
    response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
