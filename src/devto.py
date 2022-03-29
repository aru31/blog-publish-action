import requests
from custom_exceptions import MissingFrontmatterException


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
        print(response)
    else:
        print('Article Posted. ID:{} /n Created at:{}'.format(response.get("id"),
              response.get("created_at")))


def devto_update():
    pass
