import sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET
ns={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom'}
q=sys.argv[1]; n=sys.argv[2] if len(sys.argv)>2 else '15'
if q.startswith('id:'):
    url='https://export.arxiv.org/api/query?id_list='+q[3:]+'&max_results=50'
else:
    url='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(q)+'&max_results='+n
r=ET.fromstring(urllib.request.urlopen(url,timeout=60).read())
full = len(sys.argv)>3
for e in r.findall('a:entry',ns):
    t=' '.join(e.find('a:title',ns).text.split())
    i=e.find('a:id',ns).text.split('/abs/')[-1]
    au=', '.join(x.find('a:name',ns).text for x in e.findall('a:author',ns))
    s=' '.join(e.find('a:summary',ns).text.split())
    jr=e.find('x:journal_ref',ns); d=e.find('x:doi',ns)
    print(f"[{i}] {t} -- {au}" + (f" | JR: {jr.text}" if jr is not None else "") + (f" | DOI: {d.text}" if d is not None else ""))
    print("   ", s if full else s[:400]); print()
