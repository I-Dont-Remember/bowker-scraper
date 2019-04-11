# main page 
# http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/Index

# After selecting 'Bowker Adult'
# POST http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/GetChildTags
# params => tagUrl: Subjects¦Bowker Adult¦N
# Response:
# {"tags":[{"tag":"A","url":"Subjects¦Bowker Adult¦A¦Y","more":"Y"},{"tag":"B","url":"Subjects¦Bowker Adult¦B¦Y","more":"Y"},{"tag":"C","url":"Subjects¦Bowker Adult¦C¦Y","more":"Y"},{"tag":"D","url":"Subjects¦Bowker Adult¦D¦Y","more":"Y"},{"tag":"E","url":"Subjects¦Bowker Adult¦E¦Y","more":"Y"},{"tag":"F","url":"Subjects¦Bowker Adult¦F¦Y","more":"Y"},{"tag":"G","url":"Subjects¦Bowker Adult¦G¦Y","more":"Y"},{"tag":"H","url":"Subjects¦Bowker Adult¦H¦Y","more":"Y"},{"tag":"I","url":"Subjects¦Bowker Adult¦I¦Y","m…ag":"R","url":"Subjects¦Bowker Adult¦R¦Y","more":"Y"},{"tag":"S","url":"Subjects¦Bowker Adult¦S¦Y","more":"Y"},{"tag":"T","url":"Subjects¦Bowker Adult¦T¦Y","more":"Y"},{"tag":"U","url":"Subjects¦Bowker Adult¦U¦Y","more":"Y"},{"tag":"V","url":"Subjects¦Bowker Adult¦V¦Y","more":"Y"},{"tag":"W","url":"Subjects¦Bowker Adult¦W¦Y","more":"Y"},{"tag":"X","url":"Subjects¦Bowker Adult¦X¦Y","more":"Y"},{"tag":"Y","url":"Subjects¦Bowker Adult¦Y¦Y","more":"Y"},{"tag":"Z","url":"Subjects¦Bowker Adult¦Z¦Y","more":"Y"}]}

# Now have a list of each letter in alphabet, to grab underneath that->
#  Select A
# POST http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/GetChildTags
# params => tagUrl: Subjects¦Bowker Adult¦A¦Y
# Response:
# {"tags":[{"tag":"AA","url":"Subjects¦Bowker Adult¦AA¦Y","more":"Y"},{"tag":"AB","url":"Subjects¦Bowker Adult¦AB¦Y","more":"Y"},{"tag":"AC","url":"Subjects¦Bowker Adult¦AC¦Y","more":"Y"},{"tag":"AD","url":"Subjects¦Bowker Adult¦AD¦Y","more":"Y"},{"tag":"AE","url":"Subjects¦Bowker Adult¦AE¦Y","more":"Y"},{"tag":"AF","url":"Subjects¦Bowker Adult¦AF¦Y","more":"Y"},{"tag":"AG","url":"Subjects¦Bowker Adult¦AG¦Y","more":"Y"},{"tag":"AH","url":"Subjects¦Bowker Adult¦AH¦Y","more":"Y"},{"tag":"AI","url":"Subjects¦Bow…bjects¦Bowker Adult¦AT¦Y","more":"Y"},{"tag":"AU","url":"Subjects¦Bowker Adult¦AU¦Y","more":"Y"},{"tag":"AV","url":"Subjects¦Bowker Adult¦AV¦Y","more":"Y"},{"tag":"AW","url":"Subjects¦Bowker Adult¦AW¦Y","more":"Y"},{"tag":"AX","url":"Subjects¦Bowker Adult¦AX¦Y","more":"Y"},{"tag":"AY","url":"Subjects¦Bowker Adult¦AY¦Y","more":"Y"},{"tag":"AZ","url":"Subjects¦Bowker Adult¦AZ¦Y","more":"Y"},{"tag":"A ","url":"Subjects¦Bowker Adult¦A ¦Y","more":"Y"},{"tag":"A-","url":"Subjects¦Bowker Adult¦A-¦Y","more":"Y"}]}

# Now click AA
# POST http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/GetChildTags
# params => tagUrl: Subjects¦Bowker Adult¦AA¦Y
# Response:
# {"tags":[{"tag":"AACHEN (GERMANY)","url":"Subjects¦Bowker Adult¦AACHEN (GERMANY)¦N","more":"N"},{"tag":"AACHEN (GERMANY)_HISTORY","url":"Subjects¦Bowker Adult¦AACHEN (GERMANY)_HISTORY¦N","more":"N"},{"tag":"AACHEN (GERMANY)_HISTORY_SIEGE, 1944","url":"Subjects¦Bowker Adult¦AACHEN (GERMANY)_HISTORY_SIEGE, 1944¦N","more":"N"},{"tag":"AALTO, ALVAR, 1898-1976","url":"Subjects¦Bowker Adult¦AALTO, ALVAR, 1898-1976¦N","more":"N"},{"tag":"AARON (BIBLICAL PRIEST)","url":"Subjects¦Bowker Adult¦AARON (BIBLICAL PRIEST)…"Subjects¦Bowker Adult¦AARON BEN MOSES, HA-LEVI, OF STAROSIELCE, 1766-1828¦N","more":"N"},{"tag":"AARON WARD (SHIP)","url":"Subjects¦Bowker Adult¦AARON WARD (SHIP)¦N","more":"N"},{"tag":"AARON, HANK, 1934-","url":"Subjects¦Bowker Adult¦AARON, HANK, 1934-¦N","more":"N"},{"tag":"AARON, HANK, 1934-_JUVENILE LITERATURE","url":"Subjects¦Bowker Adult¦AARON, HANK, 1934-_JUVENILE LITERATURE¦N","more":"N"},{"tag":"AARONSOHN, SARAH, 1891-1917","url":"Subjects¦Bowker Adult¦AARONSOHN, SARAH, 1891-1917¦N","more":"N"}]}

# Click AACHEN, it redirects to the search for it? i guess
# POST http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/DoSearch
# params => tagUrl: Subjects¦Bowker Adult¦AACHEN (GERMANY)¦N

# Sends to 
# GET http://www.booksinprint.com.ezproxy.library.wisc.edu/Search/Results?q=subject-exact:[AACHEN+(GERMANY)]&brws=1
import requests
import json
import string
import time

# TODO: Rzko3xtOnQ5CUUu
# 3433A38A3340BFACF45CB256D6AD896D288F5CC19C545A8606580A8F964B2F836564CB885D8062A48F01D619910287D09EBC35EA0174E7AB5A3555035B99CC5A36C2F30C139616CE36E08BB6E778E741079C01D6A0C1A96B21D14A18322FF11C32402FECAEFD89590344C1DE0886036E2A5EEFC23055EBD2FCD3D2D3BB79269F7EC56C65C228A36B1B6DDEC378C16243543BD4937DC46ED4632F8A30A6ACFC3162926ADC0E4A469D9F2D3593C614CCF5E7B4FD6467E4B184B866524C876426D3310EB4548268FADD3231A1019859A826
class Client(object):
    def __init__(self, ezproxy_cookie, aspauth_cookie):
        self.ezproxy = ezproxy_cookie
        self.aspauth = aspauth_cookie

    def _post(self, url, data):
        cookies = {
            "ezproxy": "Rzko3xtOnQ5CUUu",#self.ezproxy,
            ".ASPXAUTH": "3433A38A3340BFACF45CB256D6AD896D288F5CC19C545A8606580A8F964B2F836564CB885D8062A48F01D619910287D09EBC35EA0174E7AB5A3555035B99CC5A36C2F30C139616CE36E08BB6E778E741079C01D6A0C1A96B21D14A18322FF11C32402FECAEFD89590344C1DE0886036E2A5EEFC23055EBD2FCD3D2D3BB79269F7EC56C65C228A36B1B6DDEC378C16243543BD4937DC46ED4632F8A30A6ACFC3162926ADC0E4A469D9F2D3593C614CCF5E7B4FD6467E4B184B866524C876426D3310EB4548268FADD3231A1019859A826"#self.aspauth
        }
        r = requests.post(url, data=data, cookies=cookies)
        if r.status_code != 200:
            raise ValueError("Not a 200, got %d" % r.status_code)
        else:
            return r.json()

    # Example Output
    # [
    # {'tag': 'AACHEN (GERMANY)', 'url': 'Subjects¦Bowker Adult¦AACHEN (GERMANY)¦N', 'more': 'N'},
    #  {'tag': 'AACHEN (GERMANY)_HISTORY', 'url': 'Subjects¦Bowker Adult¦AACHEN (GERMANY)_HISTORY¦N', 'more': 'N'}, 
    # {'tag': 'AACHEN (GERMANY)_HISTORY_SIEGE, 1944', 'url': 'Subjects¦Bowker Adult¦AACHEN (GERMANY)_HISTORY_SIEGE, 1944¦N', 'more': 'N'}, {'tag': 'AALTO, ALVAR, 1898-1976', 'url': 'Subjects¦Bowker Adult¦AALTO, ALVAR, 1898-1976¦N', 'more': 'N'}, {'tag': 'AARON (BIBLICAL PRIEST)', 'url': 'Subjects¦Bowker Adult¦AARON (BIBLICAL PRIEST)¦N', 'more': 'N'}, {'tag': 'AARON BEN MOSES, HA-LEVI, OF STAROSIELCE, 1766-1828', 'url': 'Subjects¦Bowker Adult¦AARON BEN MOSES, HA-LEVI, OF STAROSIELCE, 1766-1828¦N', 'more': 'N'}, {'tag': 'AARON WARD (SHIP)', 'url': 'Subjects¦Bowker Adult¦AARON WARD (SHIP)¦N', 'more': 'N'}, {'tag': 'AARON, HANK, 1934-', 'url': 'Subjects¦Bowker Adult¦AARON, HANK, 1934-¦N', 'more': 'N'}, {'tag': 'AARON, HANK, 1934-_JUVENILE LITERATURE', 'url': 'Subjects¦Bowker Adult¦AARON, HANK, 1934-_JUVENILE LITERATURE¦N', 'more': 'N'}, {'tag': 'AARONSOHN, SARAH, 1891-1917', 'url': 'Subjects¦Bowker Adult¦AARONSOHN, SARAH, 1891-1917¦N', 'more': 'N'}]
    def getSubjectsForTag(self, tag):
        url = "http://www.booksinprint.com.ezproxy.library.wisc.edu/Browse/GetChildTags"
        data = {
            "tagUrl": "Subjects¦Bowker Adult¦%s¦Y" % tag
        }
        try:
            jsonData = self._post(url, data)
            output = json.loads(jsonData)
            if not isinstance(output, dict):
                raise ValueError("Output isn't a dictionary, something is wrong")
            return output["tags"]
        except Exception as e:
            print("[!]")
            print(e)
            return []

    
def main():
    # get them goodies
    print("Subject Scraper")
    ezproxy_cookie = input("Input your ezproxy cookie: ")
    aspauth_cookie = input("Input your ASPAUTH cookie: ")
    first_letter = input("Letter to run requests against: ")
    # if len(ezproxy_cookie) == 0 or len(aspauth_cookie) == 0:
    #     print("[!] need the cookies to run on Bowker")
    #     return
    first_letter = first_letter.upper()
    if type(first_letter) is not str or len(first_letter) == 0:
        print("Need a valid letter")
        return

    client = Client(ezproxy_cookie, aspauth_cookie)

    # for AA to ZZ, some have nothing but thats ok to check if nothing there
    # or can follow letters and ignore ones with nothing
    # zb = client.getSubjectsForTag("ZB")
    letters = list(string.ascii_uppercase)
    subjects = []
    for letter in letters:
        tag = "%s%s" %(first_letter,letter)
        print(tag)
        output_list = client.getSubjectsForTag(tag)
        subjects += [x['tag'] for x in output_list]

    if not subjects:
        print("[!] no subjects found, something is wrong")
        return

    # write to a file
    filename = "subjects-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    try:
        with open(filename, 'w') as f:
            for subject in subjects:
                f.write(subject + "\n")
    except IOError as e:
        print("[!] error in writing to file")
        print(e)


if __name__ == "__main__":
    main()