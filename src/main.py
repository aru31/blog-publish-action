import sys
from custom_exceptions import WebsiteNotSupported, IndexException
from blog_publish import BlogPublishAPI
from logger import Logger

if __name__ == "__main__":
    try:
        api_key = sys.argv[1]
        website = sys.argv[2]
        owner_repo = sys.argv[3]  # aru31/test-blog-publish
        log_level = sys.argv[4]
    except IndexError as e:
        print(f"Error Message : {e}")
        raise IndexException("api_key, website, owner_repo, log_level")

    # initialising the logger
    logger_object = Logger(level=log_level)
    _logger = logger_object.logger

    if website == 'devto':
        blog_api = BlogPublishAPI(
            apikey=api_key, owner_repo=owner_repo, logger=_logger)
        blog_api.devto_publish()
    elif website == 'medium':
        blog_api = BlogPublishAPI(
            apikey=api_key, owner_repo=owner_repo, logger=_logger)
        blog_api.medium_publish()
    elif website == 'hashnode':
        blog_api = BlogPublishAPI(
            apikey=api_key, owner_repo=owner_repo, logger=_logger)
        blog_api.hashnode_publish()
    else:
        raise WebsiteNotSupported(
            "Supported websites are devto, hashnode and medium")
