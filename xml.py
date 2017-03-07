import sys
from lxml import etree, objectify


def parseLog(file):
    """
    parse xml
    """
    file = sys.argv[1]
    handler = open(file).read()
    # parser = etree.XMLParser(remove_comments=True)
    # tree = objectify.parse(file, parser=parser)
    parser = objectify.makeparser(recover=True)
    root = objectify.fromstring(handler, parser)
    print(root.attrib['venue'])
    # race_attrib = root.race.nomination
    # for k in root.race.attrib:
    #     print(k.tag, k.text)
    # for race in root.race.getchildren():
    #     for e in race.getchildren():
    #         print(e.tag, e.text)
    # for race in stuff.getchildren():
    #     race_attrib = race.attrib
    #     print(race_attrib)
    attrs = [
        'id', 'number', 'horse', 'barrier', 'weight', 'goodtrack',
        'thisdistance', 'firstup', 'secondup', 'decimalmargin'
    ]
    for noms in root.race:
        print("#######################################")
        print('id', 'number', 'horse', 'barrier', 'weight', 'goodtrack',
              'thisdistance')
        print(noms.attrib.get('id'))
        for item in noms.nomination:
            try:
                listy = [item.attrib[x] for x in attrs]
                listy.insert(0, noms.attrib.get('id'))
                print(listy)
            except KeyError:
                continue


if __name__ == "__main__":
    parseLog(sys.argv[1])
