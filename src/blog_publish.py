from asyncio.log import logger
import frontmatter
from urllib import request
from devto import devto_create
from medium import medium_create
from hashnode import hashnode_create
from findfiles import FindFiles
from constants import (
    API_URLS,
    MESSAGES
)
from custom_exceptions import (
    WrongURLException
)


class BlogPublishAPI(object):
    def __init__(self, apikey, owner_repo, logger):
        self.logger = logger
        self.parsedfiles = list()

        """
        parsed files schema: 
        [
            {
                "fileinfo": {
                    "filename": "hello.md",
                    "url": "http://...",
                    "status": "..."
                },
                "metadata": {
                    "title": "Lorum Ipsum",
                    "description": "Lorum Ipsum Lorum Ipsum",
                    ...,
                    ...,
                    ...
                },
                "content: "Lorum Ipsum Lorum Ipsum Lorum Ipsum"
            },
            {}
        ]
        """

        self.apikey = apikey
        self.owner_repo = owner_repo
        self.get_all_required_parsed_files()

    def download_file(self, url, filename):
        try:
            # downloading the file with the same name will override the previous file
            request.urlretrieve(url, "blog.md")
            self.logger.debug(f"Downloading file -> {filename}")
        except Exception as e:
            self.logger.error(f"Error message : {e}")
            raise WrongURLException(url)

    def parse_and_create_fileinfo(self, file_info):
        """
        parse the .md file to separate body (content) from frontmatter (metadata)
        """

        self.logger.debug("Parsing the markdown file")
        with open("blog.md") as f:
            _metadata, _content = frontmatter.parse(f.read())

        self.logger.debug("Creating the parsed files dict")
        _parseddict = {
            "fileinfo": file_info,
            "metadata": _metadata,
            "content": _content
        }
        self.parsedfiles.append(_parseddict)

    def get_all_required_parsed_files(self):
        """
        Parse all the required files
        """

        findfiles = FindFiles(owner_repo=self.owner_repo, logger=self.logger)

        """
        files sample schema: 
        [
            {'filename': 'test_blog.md', 'url': '....', 'status': 'modified'},
            {...}
        ]
        """
        files = findfiles.useful_files

        # iterating through all the files (list of dictionaries)
        for file_info in files:
            self.download_file(
                url=file_info["url"], filename=file_info["filename"])
            self.parse_and_create_fileinfo(file_info)

    def devto_publish(self):
        for file in self.parsedfiles:
            self.logger.info(
                f"Started processing file : {file['fileinfo']['filename']}")
            if file["metadata"]["publish_devto"]:
                devto_create(metadata=file["metadata"], content=file["content"],
                             apikey=self.apikey, url=API_URLS.DEVTO, logger=self.logger)
                self.logger.info(
                    f"Completed processing file : {file['fileinfo']['filename']}")
            else:
                self.logger.warning(
                    f"{MESSAGES.notpublishmessage} dev.to. publish_devto was set to false")

    def medium_publish(self):
        for file in self.parsedfiles:
            self.logger.info(
                f"Started processing file : {file['fileinfo']['filename']}")
            if file["metadata"]["publish_medium"]:
                medium_create(metadata=file["metadata"], content=file["content"],
                              apikey=self.apikey, url=API_URLS.MEDIUM, logger=self.logger)
                self.logger.info(
                    f"Completed processing file : {file['fileinfo']['filename']}")
            else:
                self.logger.warning(
                    f"{MESSAGES.notpublishmessage} medium. publish_medium was set to false")

    def hashnode_publish(self):
        hashnode_create()
