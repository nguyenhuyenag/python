from xml.dom.minidom import parse
import xml.dom.minidom as _minidom

DOMTree = _minidom.parse("D:/advanced/day3/files/student.xml")
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

students = collection.getElementsByTagName("student")

for student in students:
    print("=== Student ===")
    if student.hasAttribute("id"):
        print("ID: %s" % student.getAttribute("id"))

    name = student.getElementsByTagName("name")[0]
    print("Name: %s" % name.childNodes[0].data)

    date = student.getElementsByTagName("date")[0]
    print("Date of birth: %s" % date.childNodes[0].data)
