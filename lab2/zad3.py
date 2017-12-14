#!/usr/bin/env python
import xml.dom.minidom


def replaceText(node, newText):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise ("node does not contain text")

    node.firstChild.nodeValue = newText


xml1 = xml.dom.minidom.parse("test.xml")

print xml1.toxml()
node = xml1.getElementsByTagName("innecos")[0]
print (node)
replaceText(node, "czosnek")
print node.firstChild.nodeValue

with (open("test.xml", 'w')) as f:
    f.write(xml1.toxml())

    f.close()
