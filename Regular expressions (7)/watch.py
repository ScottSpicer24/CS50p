'''
In a file called watch.py, implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be
equivalent as a str. Expect that any such URL will be in one of the formats below.
Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.


<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

or

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
'''
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(link):
    if re.search('^<iframe width="\d+" height="\d+" src="https?://www\.youtube\.com/embed/(\w|\d)+" title="(\w|\s)+" frameborder="\d+" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>$', link.strip()):
        url = re.search('^(.+) src="(.+)" title="(.+)$', link)
        return url.group(2).strip()
    elif re.search('^<iframe src="https?://www\.youtube\.com/embed/\w+"></iframe>$', link.strip()):
        url = re.search('^(.+) src="(.+)" title="(.+)$', link)
        return url.group(2).strip()
    else:
        return None


if __name__ == "__main__":
    main()