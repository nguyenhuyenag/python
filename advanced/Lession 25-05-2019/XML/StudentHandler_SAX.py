import xml.sax

class StudentHander(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=""
        self.ids=""
        self.name=""
        self.date=""

    def startElement(self, tag, atrributes):
        self.CurrentData=tag
        if tag=="student":
            print('*****Student****')
            ids=atrributes['id']
            print ("ID: ",ids)

    def endElement(self, tag):
        if self.CurrentData=='id':
            print("ID: ", self.ids)
        elif self.CurrentData=='name':
            print("NAME: ", self.name)
        elif self.CurrentData=='date':
            print("DATE: ", self.date)
        self.CurrentData=""
        
    def characters(self, content):
        if self.CurrentData=='id':
           self.ids= content
        elif self.CurrentData=='name':
            self.name= content
        elif self.CurrentData=='date':
            self.date= content
        
if(__name__=="__main__"):
    parser= xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    Handler= StudentHander()
    parser.setContentHandler(Handler)
    parser.parse('D:\\Lession 25-05-2019\\files\\student.xml')

