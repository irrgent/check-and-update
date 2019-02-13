import sys
from bs4 import BeautifulSoup


def get_news(html_doc):

    div = html_doc.find('div', id="news")

    if div is None:
        print("Could not find div tag with appropriate id.", file=sys.stderr)
        sys.exit(1)

    news_items = div.findChildren('h4', recursive=False)

    return news_items


def compare_news(page1, page2):

    page1_bs = BeautifulSoup(page1, features="html5lib")
    page2_bs = BeautifulSoup(page2, features="html5lib")

    page1_news = get_news(page1_bs)
    page2_news = get_news(page2_bs)

    if page1_news[0].text == page2_news[0].text:
        return 0
    else:
        return -1


def main(args):

    if len(args) != 3:
        raise ValueError("Expected 2 arguments, got {}".format(len(args) - 1))

    ret_code = compare_news(args[1], args[2])

    print(ret_code)

    sys.exit(0)


if __name__ == '__main__':

    main(sys.argv)
