class GITHUB_CODES:
    REMOVED = "removed"
    ADDED = "added"
    MODIFIED = "modified"
    RENAMED = "renamed"


class API_URLS:
    DEVTO = "https://dev.to/api/articles"
    HASHNODE = "https://api.hashnode.com/"
    MEDIUM = "https://api.medium.com/v1"
    GITHUB = "https://api.github.com/repos"


class CONSTANTS:
    FOLDER_NAME = "blogs"


class FRONTMATTER:
    TITLE = "title"
    DATE = "date"
    DESCRIPTION = "description"
    TAGS = "tags"
    DEVTO_SERIES = "devto_series"
    HASHNODE_PUBLICATION_ID = "hashnode_publication_id"
    PUBLISH_DEVTO = "publish_devto"
    PUBLISH_MEDIUM = "publish_medium"
    PUBLISH_HASHNODE = "publish_hashnode"


class Messages:
    @classmethod
    def notpublishmessage(cls, website, variable):
        notpublishmessage = f"""
        Either you didn't want to publish the article on {website} 
        and set {variable} to false in markdown frontmatter
        or you forgot to set {variable} in markdown frontmatter
        or you have used the wrong variable format it should be {variable}: True
        """
        return notpublishmessage

    @classmethod
    def nopublicationidmessage(cls, variable):
        nopublicationidmessage = f"""
        No publication id was provided in the frontmatter of the updloaded markdown file 
        The format is {variable}: id
        """
        return nopublicationidmessage
