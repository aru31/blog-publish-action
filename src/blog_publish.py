import frontmatter
from urllib import request
from devto import devto_create
from findfiles import FindFiles
from constants import GITHUB_CODES, API_URLS
from custom_exceptions import UpdationNotImplemented, WrongURLException


class BlogPublishAPI(object):
    def __init__(self, apikey):
        self.content = None
        self.metadata = None
        self.apikey = apikey

    def download_file(self, url, filename):
        try:
            # downloading the file with the same name will override the previous file
            request.urlretrieve(url, "blog.md")
            # check if this logging works in the GitHub console
            print(f"Downloading file -> {filename}")
        except Exception as e:
            print(f"Error message : {e}")
            raise WrongURLException(url)

    def parse_md(self):
        """
        parse the .md file to separate body (content) from frontmatter (metadata)
        """

        with open("blog.md") as f:
            self.metadata, self.content = frontmatter.parse(f.read())

    def devto_publish(self):
        """
        Dev.to publish
        """

        findfiles = FindFiles()
        files = findfiles.useful_files

        # iterating through all the files (list of dictionaries)
        for file_info in files:
            self.download_file(
                url=file_info["url"], filename=file_info["filename"])
            self.parse_md()

            if file_info["status"] == GITHUB_CODES.ADDED:
                devto_create(metadata=self.metadata, content=self.content,
                             apikey=self.apikey, url=API_URLS.DEVTO)
            if file_info["status"] == GITHUB_CODES.MODIFIED:
                raise UpdationNotImplemented("dev.to")
