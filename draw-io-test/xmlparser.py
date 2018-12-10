from lxml import etree
from io import StringIO


class XmlParser(object):
    def getTreeFromFile(self, fullName):
        root = etree.parse(fullName)
        diagramElement = root.find('diagram')
        assert diagramElement is not None
        return diagramElement.text

    def getRefTreeFromFile(self, fullName):
        root = etree.parse(fullName)
        assert root is not None
        return root

    def getTreeFromString(self, data):
        jim = etree.fromstring(data)
        return jim

    def compareGeometries(self, refTree, decTree):
        refGeo = refTree.findall('.//mxGeometry')
        decGeo = decTree.findall('.//mxGeometry')
        assert refGeo is not None
        assert decGeo is not None
        geo1 = refGeo[0].attrib == decGeo[0].attrib
        geo2 = refGeo[1].attrib == decGeo[1].attrib
        return geo1 & geo2
