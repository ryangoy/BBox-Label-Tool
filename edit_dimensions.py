import xml.etree.ElementTree as ET
import os
import sys
from xml.dom import minidom
from xml.etree.ElementTree import tostring

def prettify(elem):
    """Return a pretty-printed XML string
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

if len(sys.argv) < 2:
    print 'Usage:'
    print '\t' + argv[0] + ' <directory>'

for i in os.listdir(sys.argv[1]):
    if i == '.DS_Store' or i == '.xml':
        continue
    tree = ET.parse(os.path.join(sys.argv[1], i))
    root = tree.getroot()
    size = root.find('size')
    width = size.find('width')
    width.text = '900'
    height = size.find('height')
    height.text = '753'
    output = prettify(root)
    save_name = os.path.join(sys.argv[1], i)
    with open(save_name, 'w') as f:
        f.write(output[output.index('\n')+1:])


