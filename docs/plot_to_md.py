import meshplot
import json

total = ""
first = True

def mp_to_md(self):
    global total
    global first
    res = self.to_html()
    first = False

    total += "aaaaa\n"+res
    with open('export.html', 'w') as fp:
            fp.write(total)
    return res

get_ipython().display_formatter.formatters["text/html"].for_type(meshplot.Viewer, mp_to_md)
