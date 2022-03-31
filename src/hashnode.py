import requests
from custom_exceptions import MissingFrontmatterException
from constants import FRONTMATTER


def hashnode_create(metadata, content, apikey, url, logger):
    logger.info("Preparing to send the blogs to hashnode")

    query = """
        mutation CreatePublicationStoryName($input:CreateStoryInput! , $publicationId: String!){
            createPublicationStory(input: $input, publicationId: $publicationId){
                code
                success
                message
                post {
                    slug
                }
            }
        }
    """

    try:
        createStoryInput = {
            'title': metadata[FRONTMATTER.TITLE],
            'contentMarkdown': content,
            'tags': []
        }
    except Exception as e:
        logger.error(f"Error Message : {e}")
        raise MissingFrontmatterException
    logger.debug("createStoryInput successfully formed")

    variables = {
        'input': createStoryInput,
        'publicationId': metadata[FRONTMATTER.HASHNODE_PUBLICATION_ID]
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': apikey
    }

    response = requests.post(
        url, json={'query': query, 'variables': variables}, headers=headers).json()

    if response.get('data') == None:
        logger.error("Some error occured while making the request")
        logger.error(f"Official response returned : {response}")
    else:
        logger.warning(
            "Please check the response to determine if the request succeeded or failed")
        logger.warning(f"Official response returned : {response}")
