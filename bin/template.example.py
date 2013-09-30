#!/usr/bin/python

from string import Template

template_file='/var/websites/templates/page.templ'

template_content = open(template_file, "r").read()
template_object = Template(template_content)
template_values = dict( title           = "Offene Bestellungen",
                        additional_head = "",
                        body_headline  = "Offene Bestellungen",
                        body           = "Erich bestellt 1 Krug",
                        body_footer    = "",
                      )
template_filled = template_object.substitute(template_values)

print template_filled
