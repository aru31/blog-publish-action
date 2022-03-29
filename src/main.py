import sys
from custom_exceptions import WebsiteNotSupported, IndexException
from blog_publish import BlogPublishAPI

if __name__ == "__main__":
    try:
        api_key = sys.argv[1]
        website = sys.argv[2]
    except IndexError as e:
        print(f"Error Message : {e}")
        raise IndexException("api_key, website")

    if website == 'devto':
        c = BlogPublishAPI(sys.argv[1])
        c.devto_publish()
    else:
        raise WebsiteNotSupported
