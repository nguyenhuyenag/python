from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree=xml.dom.minidom.parse('D:\\Lession 25-05-2019\\files\\student.xml')
Document=DOMTree.documentElement
if(Document.hasAttribute('shelf')):
    print ('Root element: %s' %Document.getAttribute("shelf"))
liststudents= Document.getElementsByTagName("student")
for student in liststudents:
    print("********Student*********")
    if student.hasAttribute('id'):
        print(student.getAttribute('id'))
    name = student.getElementsByTagName('name')[0]
    print ("Name: %s" % name.childNodes[0].data)
    date = student.getElementsByTagName('date')[0]
    print ("Date of birth: %s" % date.childNodes[0].data)