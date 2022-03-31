import frontmatter
from urllib import request

from sites.devto import devto_create
from sites.medium import medium_create
from sites.hashnode import hashnode_create
from utils.findfiles import FindFiles
from constants.constants import (
    API_URLS,
    Messages,
    FRONTMATTER
)
from utils.custom_exceptions import (
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
            if file.get("metadata").get(FRONTMATTER.PUBLISH_DEVTO) != None:
                devto_create(metadata=file["metadata"], content=file["content"],
                             apikey=self.apikey, url=API_URLS.DEVTO, logger=self.logger)
                self.logger.info(
                    f"Completed processing file : {file['fileinfo']['filename']}")
                self.logger.info("-----------------")
            else:
                message = Messages.notpublishmessage(
                    website="devto", variable=FRONTMATTER.PUBLISH_DEVTO)
                self.logger.warning(message)
                self.logger.warning(
                    f"Skipping processing of file : {file['fileinfo']['filename']}")
                self.logger.info("-----------------")

    def medium_publish(self):
        for file in self.parsedfiles:
            self.logger.info(
                f"Started processing file : {file['fileinfo']['filename']}")
            if file.get("metadata").get(FRONTMATTER.PUBLISH_MEDIUM) != None:
                medium_create(metadata=file["metadata"], content=file["content"],
                              apikey=self.apikey, url=API_URLS.MEDIUM, logger=self.logger)
                self.logger.info(
                    f"Completed processing file : {file['fileinfo']['filename']}")
                self.logger.info("-----------------")
            else:
                message = Messages.notpublishmessage(
                    website="medium", variable=FRONTMATTER.PUBLISH_MEDIUM)
                self.logger.warning(message)
                self.logger.warning(
                    f"Skipping processing of file : {file['fileinfo']['filename']}")
                self.logger.info("-----------------")

    def hashnode_publish(self):
        for file in self.parsedfiles:
            self.logger.info(
                f"Started processing file : {file['fileinfo']['filename']}")
            if file.get("metadata").get(FRONTMATTER.PUBLISH_HASHNODE) != None:
                if file.get("metadata").get(FRONTMATTER.HASHNODE_PUBLICATION_ID) != None:
                    hashnode_create(metadata=file["metadata"], content=file["content"],
                                    apikey=self.apikey, url=API_URLS.HASHNODE, logger=self.logger)
                    self.logger.info(
                        f"Completed processing file : {file['fileinfo']['filename']}")
                    self.logger.info("-----------------")
                else:
                    message = Messages.nopublicationidmessage(
                        variable=FRONTMATTER.HASHNODE_PUBLICATION_ID)
                    self.logger.warning(message)
                    self.logger.warning(
                        f"Skipping processing of file : {file['fileinfo']['filename']}")
                    self.logger.info("-----------------")
            else:
                message = Messages.notpublishmessage(
                    website="hashnode", variable=FRONTMATTER.PUBLISH_HASHNODE)
                self.logger.warning(message)
                self.logger.warning(
                    f"Skipping processing of file : {file['fileinfo']['filename']}")
                self.logger.info("-----------------")
