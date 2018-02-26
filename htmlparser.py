from HTMLParser import HTMLParser, HTMLParseError
import re
import logging


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(lineno)s - %(levelname)s: %(message)s", datefmt='%Y.%m.%d %H:%M:%S')


class SomeHtmlParser(HTMLParser):
    """Parses HTTP response text to remove HTML tags"""
    def __init__(self):
        HTMLParser.__init__(self)
        self.body_text = []
        self.in_ignored_element = False
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
        if self.in_body and re.match(r'script|svg|style', tag):
            self.in_ignored_element = True

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_body = False
        if self.in_body and re.match(r'script|svg|style', tag):
            self.in_ignored_element = False

    def handle_data(self, data):
        if not self.in_ignored_element and self.in_body:
            stripped_data = data.strip()
            if len(stripped_data) > 0:
                self.body_text.append(stripped_data)


def parse_http_error(text):
    if re.match(r'<.*?>', "".join(text.strip().splitlines())):
        p = SomeHtmlParser()
        try:
            p.feed(text)
            return ' '.join(p.body_text)
        except HTMLParseError:
            log.info("Encountered error in parsing")
    return text


# some_string = u'Nothing is wrong here'
# some_string = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>test</title></head><body><a href="http://www.example.com?a=1&b=2">Hello &amp; World</a></body></html>'
# some_string = '<span class="email" data-href="mailto:&quot;John Doe&quot; &lt;john.doe@example.com&gt;">'
# some_string = '<ht fldf d><'
# some_string = "<script>hello</script>"
# some_string = """
# <SEC-DOCUMENT>0001005214-12-000007.txt : 20120430
# <SEC-HEADER>0001005214-12-000007.hdr.sgml : 20120430
# <ACCEPTANCE-DATETIME>20120430163103
# ACCESSION NUMBER:       0001005214-12-000007
# CONFORMED SUBMISSION TYPE:  10-K
# PUBLIC DOCUMENT COUNT:      12
# CONFORMED PERIOD OF REPORT: 20120131
# FILED AS OF DATE:       20120430
# DATE AS OF CHANGE:      20120430
#
# FILER:
#
#     COMPANY DATA:
#         COMPANY CONFORMED NAME:         AMERICAN WAGERING INC
#         CENTRAL INDEX KEY:          0001005214
#         STANDARD INDUSTRIAL CLASSIFICATION: SERVICES-MISCELLANEOUS AMUSEMENT & RECREATION [7990]
#         IRS NUMBER:             880344658
#         STATE OF INCORPORATION:         NV
#         FISCAL YEAR END:            0105
#
#     FILING VALUES:
#         FORM TYPE:      10-K
#         SEC ACT:        1934 Act
#         SEC FILE NUMBER:    000-20685
#         FILM NUMBER:        12795496
#
#     BUSINESS ADDRESS:
#         STREET 1:       675 GRIER DR
#         CITY:           LAS VEGAS
#         STATE:          NV
#         ZIP:            89119
#         BUSINESS PHONE:     7027350101
#
#     MAIL ADDRESS:
#         STREET 1:       675 GRIER DR
#         CITY:           LAS VEGAS
#         STATE:          NV
#         ZIP:            89119
# </SEC-HEADER>
# <DOCUMENT>
# <TYPE>10-K
# <SEQUENCE>1
# <FILENAME>formtenk-01312012.htm
# <DESCRIPTION>FORM 10 K 1.31.2012
# <TEXT>
# <html>
# <head>
# """
# some_string = u'<html><body><h1>503 Service Unavailable</h1>\nNo server is available to handle this request.\n</body></html>\n'
# some_string = '''
#     <html>
#     <head>
#     <title>
#     A Simple HTML Document
#     </title>
#     </head>
#     <body>
#     <p>\tThis is a <b>very</b> simple HTML document</p>
#     <svg>svg data</svg>
#     <hr>
#     <form>
#     Some text input: <input type="text">
#     </form>
#     <br>
#     <!-- some comment -->
#     <table>
#     <th>header</th>
#     </table>
#     <button>Click me!</button>
#     <ul>
#     <li>hi</li>
#     </ul>
#     <script>console.log('hello');</script>
#     <h3>header3</h3>
#     <p>It only has two paragraphs</p>
#     </body>
# '''
print parse_http_error(some_string)
