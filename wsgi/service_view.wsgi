import sys, time
from string import Template
sys.path.append("/var/websites/lib/")
import datastore

def application(environ, start_response):
    template_file='/var/websites/templates/page.templ'
    template_content = open(template_file, "r").read()
    template_object = Template(template_content)

    template_values = dict( title           = "Offene Bestellungen",
                            additional_head = "",
                            body_class      = "",
                            body_headline   = "Offene Bestellungen",
                            body            = "",
                            body_footer     = "",
                          )

    open_order_sum = 0
    open_orders = datastore.get_orders( {"status": [0]} )

    # build the main table
    row_color = 0;
    template_values['body'] += '<table>\n'
    template_values['body'] += '    <tr><th>Wer</th><th>Was</th><th>bestellt um</th><th>ID</th></tr>\n'

    for row in open_orders:
        template_values['body'] += "   <tr class=line%s><td>%s</td><td>%s %s</td><td>%s</td><td>%s</td></tr>\n" % (row_color, row[1], row[3], row[2], time.strftime("%H:%M Uhr am %d.%m.%Y", time.localtime(row[5])), row[0])
        open_order_sum += row[3]
	row_color = (row_color + 1) % 2;

    template_values['body'] += '</table>\n'

    if open_order_sum == 0:
        template_values['body'] = '<p class="sum">Keine</p>'
        template_values['body_class'] = 'class="bg_green"'
    else:
        template_values['body'] += '<p class="sum">Insgesamt %s Bestellungen offen</p>' % open_order_sum
        template_values['body_class'] = 'class="bg_orange"'

    # fill in template
    template_filled = template_object.substitute(template_values)
    template_filled = template_filled.encode('utf-8')

    # fill in HTTP headers and return all together
    status = '200 OK' 
    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(template_filled)))]
    start_response(status, response_headers)

    return [template_filled]



