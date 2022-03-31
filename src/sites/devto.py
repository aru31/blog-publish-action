import requests
from utils.custom_exceptions import MissingFrontmatterException
from constants.constants import *


def devto_create(metadata, content, apikey, url, logger):
    """
    DevTo Publish API
    Reference -> https://developers.forem.com/api#operation/createArticle

    Create an article
    :param title: Title
    :param body_markdown: Article Markdown content
    :param published: True to create published article, false to create a draft
    :param series: Article series name
    :param main_image: Main image (or cover image)
    :param tags: List of article tags
    """

    logger.info("Preparing to send the blogs to dev.to")
    try:
        data = {
            "article": {
                "title": metadata[FRONTMATTER.TITLE],
                "body_markdown": content,
                "published": metadata[FRONTMATTER.PUBLISH_DEVTO],
                "series": metadata.get(FRONTMATTER.DEVTO_SERIES),
                "main_image": None,
                "canonical_url": None,
                "description": metadata[FRONTMATTER.DESCRIPTION],
                "tags": metadata[FRONTMATTER.TAGS],
                "organization_id": None
            }
        }
    except Exception as e:
        logger.error(f"Error Message : {e}")
        raise MissingFrontmatterException
    logger.debug(
        "Data dictionary formed successfully: means metadata was complete")

    # remove None keys from dict
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(url, json=data, headers={
                             "api-key": apikey}).json()

    if response.get("id") == None:
        custom_error_message = """
        Dev.to is horrible in returning the messages and status code, I expect two reasons, 
        either the API key is incorrect or an article with the same title and body already exists.
        """
        logger.error(custom_error_message)
        logger.error(f"Official response returned : {response}")
    else:
        logger.info(f"Article post successful")
        logger.debug(f"Article ID : {response.get('id')}")
        logger.info(f"Article URL : {response.get('url')}")
