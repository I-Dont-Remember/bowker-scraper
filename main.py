import requests
from bs4 import BeautifulSoup
import cookielib
import urllib
import urllib2
from subjects import subject_list

# parsed querystring
# {'q': ['subject-all=[Conduct of Life] {{(publisher-date=[2000-01-01~To~2000-12-31])}}'], 'ast': ['se']}
old = "http://www.booksinprint.com.ezproxy.library.wisc.edu/Search/Results?q=subject-all%3D[Conduct%20of%20Life]%20%7B%7B(publisher-date%3D[2000-01-01~To~2000-12-31])%7D%7D&ast=se"
# print(parse_qs("q=subject-all%3D[Conduct%20of%20Life]%20%7B%7B(publisher-date%3D[2000-01-01~To~2000-12-31])%7D%7D&ast=se"))

# # using httpie it sends me to netid login page, need to find a way around that
# cookies = {
#     #".ASPXAUTH": "45BBC1B99A6830F12B6567AEB47A74A615516188F849A7FBBC1D9CED8C5BBCB2B221CB8BE0698B92D9BE28C494E62342EBBA22E0FC811667B80613B772B5015F691D9CEC8904EFF0FB2C2B8259171199F1106BFF2F856E29366FEB6B3A1A81E167CDD4B86FACFFA44E94AC2A4F6216B2DC3F7C4FDBBC6B08D763CA46FC6E28256B139D2C0200686BA66F274E5DD5A5E6FD7610B98016D3362F260B59D997A9C9EB8A55CE384E1944DD4B4B1195F007A975A7BC0A64FDD45EED03216E3B1ED830C1E1E27B3E81A592E5C69BCE96B1A79D",
#     #"ezproxy": "YvTB0BRT4uq2sqB"
# }

# acquire necessary cookie for access
def login():
    cookie = ""
    return cookie


def acquire_page(cookie, query):
    base_url = "http://www.booksinprint.com.ezproxy.library.wisc.edu"
    path = "/Search/Results"
    # TODO: find out if this is the cookie we need
    cookies = {
        "ezproxy": cookie
    }
    resp = requests.get(base_url + path, params=query, cookies=cookies)

def main():
    # cookie = login()

    # query = {
    #     "q": "subject-all-[%s] {{(publisher-date=[%s~To~%s])}}" %(subject, start_date, end_date),
    #     "ast": "se"
    # }

    # page = acquire_page(cookie, query)

# fat file, so it takes a long time for BeautifulSoup to load it in,
# if this needs to be run a lot would want to find a way to minimize time/downloads

    # possibly use urllib2 to get page straight from website not a file
    # couldn't get the cookies to work ends in SSL: CERTIFICATE_VERIFY_FAILED
    # https://stackoverflow.com/questions/13925983/login-to-website-using-urllib2-python-2-7
"""
    # Store the cookies and create an opener that will hold them
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Add our headers
    opener.addheaders = [('User-agent', 'LibraryTesting')]

    # Install our opener (note that this changes the global opener to the one
    # we just made, but you can also just call opener.open() if you want)
    urllib2.install_opener(opener)

    # The action/ target from the form
    authentication_url = 'https://account.library.wisc.edu'

    # Input parameters we are going to send
    payload = {
    'op': 'login-main',
    'user': '<username>',
    'passwd': '<password>'
    }

    # Use urllib to encode the payload
    data = urllib.urlencode(payload)

    # Build our Request object (supplying 'data' makes it a POST)
    req = urllib2.Request(authentication_url, data)

    # Make the request and read the response
    page = urllib2.urlopen(old)
    soup = BeautifulSoup(page, "html.parser")
    print soup
    # <span id="resultsCount">Showing 1- 25 of 889</span>
    result_span = soup.find("span", {"id": "resultsCount"})
    words = result_span.text
    words_split = words.split(" ")
    total = words_split[-1]

    print("Total: " + total)
"""

    with open("example.html", "rb") as f:
        soup = BeautifulSoup(f, "html.parser")

        # <span id="resultsCount">Showing 1- 25 of 889</span>
        result_span = soup.find("span", {"id": "resultsCount"})
        words = result_span.text
        words_split = words.split(" ")
        total = words_split[-1]

        print("Total: " + total)

if __name__ == "__main__":
    main()


# able to login with NetID and get cookie or have user do it

# use cookie to acquire page, check that we got what we expected

# scrape the page
