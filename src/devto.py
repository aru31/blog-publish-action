import requests
from custom_exceptions import MissingFrontmatterException, UpdationWillNotBeImplemented


def devto_create(metadata, content, apikey, url):
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

    try:
        data = {
            "article": {
                "title": metadata['title'],
                "body_markdown": content,
                "published": metadata["published"],
                "series": metadata["devto_series"],
                "main_image": None,
                "canonical_url": None,
                "description": metadata['description'],
                "tags": metadata['tags'],
                "organization_id": None
            }
        }
    except Exception as e:
        print(f"Error Message : {e}")
        raise MissingFrontmatterException

    # remove None keys from dict
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(url, json=data, headers={
                             "api-key": apikey}).json()

    if response.get("id") == None:
        custom_error_message = """
        Dev.to is horrible in returning the messages and status code, I expect two reasons, 
        either the API key is incorrect or an article with the same title and body already exists.
        """
        print(custom_error_message)
        print(f"Official response returned : {response}")
    else:
        print(f"Article post successful")
        print(f"Article ID : {response.get('id')}")
        print(f"Article URL : {response.get('url')}")


def devto_update():
    reason = """
    Updation will not be implemented for dev.to since if the title or body is same it returns error.
    In the error response ID of the already existing post is not returned. 
    Only solution is to get all the posts and then go through all of them to match either the title or body.
    Bad design by dev.to
    """
    print(reason)
    raise UpdationWillNotBeImplemented("dev.to")
