import sys
from custom_exceptions import WebsiteNotSupported, IndexException
from blog_publish import BlogPublishAPI

if __name__ == "__main__":
    try:
        api_key = sys.argv[1]
        website = sys.argv[2]
        owner_repo = sys.argv[3]  # aru31/test-blog-publish
    except IndexError as e:
        print(f"Error Message : {e}")
        raise IndexException("api_key, website, owner_repo")

    if website == 'devto':
        blog_api = BlogPublishAPI(apikey=api_key, owner_repo=owner_repo)
        blog_api.devto_publish()
    elif website == 'medium':
        blog_api = BlogPublishAPI(apikey=api_key, owner_repo=owner_repo)
        blog_api.medium_publish()
    else:
        raise WebsiteNotSupported