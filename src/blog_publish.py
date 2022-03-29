import frontmatter
from devto import devto


class BlogPublishAPI(object):
    def __init__(self, apikey):
        """
        BlogPublishAPI Init Block
        """

        self.content = None
        self.metadata = None
        self.apikey = apikey
        self.parse_md()

    def parse_md(self):
        """
        parse the .md file
        """

        with open("blog.md") as f:
            self.metadata, self.content = frontmatter.parse(f.read())

    def devto_publish(self):
        """
        Dev.to publish
        """

        devto(self.metadata, self.content, self.apikey)
