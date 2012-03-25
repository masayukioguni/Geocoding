#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 緯度経度/地名の相互変換
"""


import urllib
import urllib2
import xml.dom.minidom

class diditGeoLib:
  """ test """
  def __init__(self):
    """ test """

  def _getText(self,node):
      if not node:
          return None
      for n in node.childNodes:
          if n.nodeType in [node.TEXT_NODE, node.COMMENT_NODE,node.CDATA_SECTION_NODE]:
              return n.data
          else:
              return None

  def _parse_content(self,content):
    count = 0
    doc = xml.dom.minidom.parseString(content)
    address = None
    for elem in doc.getElementsByTagName('Item'):
        addr = self._getText(elem.getElementsByTagName('Address').item(0))
        if addr:
            return addr
        return self._getText(elem.getElementsByTagName('AddressShort').item(0))
    return None

  #緯度経度から場所名取得
  def regeocoding(self,lat,lon):
      
    url = 'http://geocode.didit.jp/reverse/'
    url = url + '?lat=' + str(lat) + '&lon=' + str(lon)

    result = urllib2.urlopen(url)
    if result.code != 200:
      return None
    content = result.read()
    result.close()

    return self._parse_content(content)
   
def main():
  gl = diditGeoLib()  
  print gl.regeocoding(40,140)
  print gl.regeocoding(-40,-140)

  pass
if __name__ == "__main__":
  main()

