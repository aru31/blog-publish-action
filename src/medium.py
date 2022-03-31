import requests
from custom_exceptions import MissingFrontmatterException
from constants import FRONTMATTER


def medium_create(metadata, content, apikey, url, logger):
    """
    Medium create blog
    """

    logger.info("Preparing to send the blogs to medium")

    # header required
    header = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding"	: "gzip, deflate, br",
        "Accept-Language"	: "en-US,en;q=0.5",
        "Connection"	: "keep-alive",
        "Host"	: "api.medium.com",
        "TE"	: "Trailers",
        "Upgrade-Insecure-Requests":	"1",
        "User-Agent":	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }

    try:
        data = {
            "title": metadata[FRONTMATTER.TITLE],
            "contentFormat": "markdown",
            "content": content,
            "tags": metadata[FRONTMATTER.TAGS],
            "publishStatus": "public"
        }
    except Exception as e:
        print(f"Error Message : {e}")
        raise MissingFrontmatterException

    logger.debug(
        "Data dictionary formed successfully: means metadata was complete")

    # remove None keys from dict
    data = {k: v for k, v in data.items() if v is not None}

    # get user id from medium
    logger.debug("Getting User ID from medium")
    response_userid = requests.get(
        url=url + "/me",  # https://api.medium.com/me
        headers=header,
        params={"accessToken": apikey},
    )

    # checking response from server
    if response_userid.status_code == 200:
        logger.debug("Got the user id")
        response_userid = response_userid.json()
        userId = response_userid["data"]["id"]
        response = requests.post(
            # https://api.medium.com/me/users/{userId}/posts
            url=f"{url}/users/{userId}/posts",
            headers=header,
            params={"accessToken": apikey},
            data=data
        )

        response = response.json()
        if response.get("data") != None:
            logger.info(f"Article post successful")
            logger.debug(f"Article ID : {response['data']['id']}")
            logger.info(f"Article URL : {response['data']['url']}")
        else:
            logger.error(f"Official response returned for publish: {response}")
    else:
        logger.error(
            f"Official response returned for userid: {response_userid}")
