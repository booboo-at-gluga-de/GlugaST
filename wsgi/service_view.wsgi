import sys, time
sys.path.append("/var/websites/lib/")
import datastore

def application(environ, start_response):
    status = '200 OK' 

    output = 'Hallo Service!\n\n'
    open_order_sum = 0
    open_orders = datastore.get_orders( {"status": [0]} )
    for row in open_orders:
        output += "%s will %s %s (bestellt um %s), ID=%s\n" % (row[1], row[3], row[2], time.strftime("%H:%M Uhr am %d.%m.%Y", time.localtime(row[5])), row[0])
        open_order_sum += row[3]

    if open_order_sum == 0:
        output += "Derzeit sind keine Bestellungen offen"
    else:
        output += "\nInsgesamt %s Bestellungen offen" % open_order_sum

    output = output.encode('utf-8')
    response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
