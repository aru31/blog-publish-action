from numpy import var


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


class Messages:
    def __init__(self, website, variable):
        self.notpublishmessage = f"""
        Either you didn't want to publish the article on {website} 
        and set {variable} to false in markdown frontmatter
        or you forgot to set {variable} in markdown frontmatter
        or you have used the wrong variable format it should be {variable}: True
        """
