from xml.dom.minidom import parse
import xml.dom.minidom
import os.path

def make_xml(ten_file):
    if(os.path.isfile(ten_file)):
        doc= xml.dom.minidom.parse(ten_file)
        root_xml=doc.documentElement
    else:
        doc = Document()
        root_xml=doc.createElement('books')
        doc.appendChild(root_xml)
    child_node= doc.createElement('book')
    noi_dung="Duong xa con hat"
    child_node.setAttribute('title', noi_dung)
    root_xml.appendChild(child_node)

if __name__=='__main__':
    make_xml('book.xml').write(open(file='book.xml',mode ='w',encoding='utf8',ident='',addindent='',newl=''))