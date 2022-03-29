import requests
from pprint import pprint


def devto(metadata, content, apikey):
    """
    DevTo Publish API
    Create an article
    :param title: Title
    :param body_markdown: Article Markdown content
    :param published: True to create published article, false otherwise
    :param series: Article series name
    :param main_image: Main image (or cover image)
    :param tags: List of article tags
    :return: newly created article
    """

    url = "https://dev.to/api/articles"
    data = {
        "article": {
            "title": metadata['title'],
            "description": metadata['description'],
            "body_markdown": content,
            "tags": metadata['tags'],
            "main_image": None,
            "series": metadata["devto_series"],
            "published": metadata["published"]
        }
    }
        # remove None keys from dict
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(url, json=data, headers={"api-key":apikey}).json()

    if response.get("id") == None:
        print(response)
    else:
        print('Article Posted. ID:{} /n Created at:{}'.format(response.get("id"),response.get("created_at")))