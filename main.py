import argparse
import requests
from bs4 import BeautifulSoup
from subjects import subject_list
import datetime
import os.path
import time

global_cookie = ""

# login uses saml, which is a huge suck to do in a script i guess
# able to login with NetID and get cookie or have user do it
# saml is apparently more annoying to impersonate than just making a single request (at least so far)
# https://stackoverflow.com/questions/16512965/logging-into-saml-shibboleth-authenticated-server-using-python
# https://stackoverflow.com/questions/52618451/python-requests-saml-login-redirect
# https://stackoverflow.com/questions/22857889/ssl-error-using-python-requests-to-access-shibboleth-authenticated-server

# parsed querystring
# {'q': ['subject-all=[Conduct of Life] {{(publisher-date=[2000-01-01~To~2000-12-31])}}'], 'ast': ['se']}
old = "http://www.booksinprint.com.ezproxy.library.wisc.edu/Search/Results?q=subject-all%3D[Conduct%20of%20Life]%20%7B%7B(publisher-date%3D[2000-01-01~To~2000-12-31])%7D%7D&ast=se"
# print(parse_qs("q=subject-all%3D[Conduct%20of%20Life]%20%7B%7B(publisher-date%3D[2000-01-01~To~2000-12-31])%7D%7D&ast=se"))

# Speed up Scraping
#https://stackoverflow.com/questions/23460169/how-to-speed-up-web-scraping-in-python
# also grab that book on web scraping we have saved somewhere

def find_result_count(page):
    total = 0
    # TODO: fat file, so it takes a long time for BeautifulSoup to load it in,
    # if this needs to be run a lot would want to find a way to minimize time/downloads
    soup = BeautifulSoup(page, "html.parser")
    no_results_div = soup.find("div", {"id": "divNoresults"})
    if no_results_div:
        print("... no results found")
        total = 0
    else:
        # example:  <span id="resultsCount">Showing 1- 25 of 889</span>
        result_span = soup.find("span", {"id": "resultsCount"})
        words = result_span.text.split(" ")
        num_books = words[-1]
        if "," in words[-1]:
            num_books = (words[-1]).replace(",", "")
        total = int(num_books)

    return total


def acquire_page(cookie, query):
    base_url = "http://www.booksinprint.com.ezproxy.library.wisc.edu"
    path = "/Search/Results"
    # TODO: this cookie works, but is it actually all we need?
    cookies = {
        "ezproxy": cookie
    }
    try:
        resp = requests.get(base_url + path, params=query, cookies=cookies)
    except requests.RequestException:
        print('[!] failed while making request')
        return None

    if resp.status_code > 300:
        print("[!] failed, got resp %d" % resp.status_code)
        return None

    print("... received page")
    return resp.content


def get_subject_total_for_year(name, year):
    print("[*] getting total for %s:%s" % (name, year))
    # date range for each subject is year-01-01 to year-12-31
    date_range = "%s-01-01~To~%s-12-31" %(year, year)

    # TODO: have to be able to handle AND queries and other special symbols
    #  ['subject-all=[Children] AND subject-all=[Management] '],  same for OR
    if "AND" in name:
        split_name = name.split(" ")
        query = {
            "q": ["subject-all=[%s] AND subject-all=[%s] {{(publisher-date=[%s])}}" %(split_name[0], split_name[2], date_range)],
            "ast": ["pr"]
        }
    elif "OR" in name:
        split_name = name.split(" ")
        if len(split_name) == 4:
            query = {
                "q": ["subject-all=[%s %s] OR subject-all=[%s] {{(publisher-date=[%s])}}" %(split_name[0], split_name[1], split_name[3], date_range)],
                "ast": ["pr"]
            }
        else:
            query = {
                "q": ["subject-all=[%s] OR subject-all=[%s] OR subject-all=[%s] OR subject-all=[%s] {{(publisher-date=[%s])}}" %(split_name[0], split_name[2], split_name[4], split_name[6], date_range)],
                "ast": ["pr"]
            }
    elif name == "Total Titles":
        query = {
            "q": ["{{(publisher-date=[%s])}}" %(date_range)],
            "ast": ["pr"]
        }
    else:
        query = {
            "q": ["subject-all=[%s] {{(publisher-date=[%s])}}" %(name, date_range)],
            "ast": ["pr"]
        }

    if global_cookie is "":
        print("[!] cookie isn't set before trying to make requests")
        raise SystemExit

    page = acquire_page(global_cookie, query)
    if not page:
        raise SystemExit

    return find_result_count(page)

def get_unique_filename():
    # create unique filename such as bowker_scraper_30_Mar_2019_000.xlsx
    count = 0
    date = datetime.datetime.now()
    workbookName = "bowker_scraper_" + str(date.day) + "_" + date.strftime("%b") + "_" + str(date.year) + "_" + "%03d" % (count) + ".csv"
    while os.path.isfile(workbookName) and count < 1000:
        count = count + 1
        workbookName = "bowker_scraper_" + str(date.day) + "_" + date.strftime("%b") + "_" + str(date.year) + "_" + "%03d" % (count) + ".csv"
    if (count >= 1000):
        print("Could not create unique filename. Exiting...")
        raise SystemExit
    return workbookName


def write_csv_headers(f):
    f.write("Year")
    for subject in subject_list:
        f.write(",%s" % (subject))
    f.write("\n")


def main():
    # 1957 - 2018
    # queries per subject 61, so we have about 77*61=4600 requests to make
    # each row in sheet is a year, so 77 requests per year
    start_year = -1
    num_years = 0
    file_name = ""
    global global_cookie

    # REMOVE ME rIJ49E0fdjudv7G
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="Year to start from.")
    parser.add_argument("number", type=int, default=10, help="Number of years to run (including start year), max of 100.")
    parser.add_argument("--file", help="CSV file to create or append to.")
    args = parser.parse_args()

    if not args.file:
        needs_headers = True
        file_name = get_unique_filename()
        print("Creating file %s" % file_name)
    else:
        file_name = args.file
        needs_headers = False

    if not (1957 <= args.year <= 2025):
        print("%d not in range 1957-2025")
        return
    else:
        start_year = args.year

    if not (1 <= args.number <= 100):
        print("%d not in range 1-100")
        return
    else:
        num_years = args.number

    global_cookie = input("Please provide the cookie necessary for requests: ")


    with open(file_name, "a") as f:
        if needs_headers:
            write_csv_headers(f)

        # num-years -1 because we include start
        print("Running for year range %d to %d" % (start_year, start_year + num_years - 1))
        # no -1 because range is non-inclusive
        for year in range(start_year, start_year + num_years):
            f.write("%d" %year)
            for subject in subject_list:
                total = get_subject_total_for_year(subject, year)
                f.write(",%d"%total)
            time.sleep(15)
            f.write("\n")

if __name__ == "__main__":
    main()


# have 77 categories with 61 requests for each, so this needs to be batched, also need to have delays so we don't overwhelm stuff
