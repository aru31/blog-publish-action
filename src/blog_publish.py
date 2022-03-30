import frontmatter
from urllib import request
from devto import devto_create, devto_update
from findfiles import FindFiles
from constants import GITHUB_CODES, API_URLS
from custom_exceptions import (
    UpdationNotImplemented,
    WrongURLException,
    DidnotWantToPublish
)


class BlogPublishAPI(object):
    def __init__(self, apikey, owner_repo):
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
            print(f"Downloading file -> {filename}")
        except Exception as e:
            print(f"Error message : {e}")
            raise WrongURLException(url)

    def parse_and_create_fileinfo(self, file_info):
        """
        parse the .md file to separate body (content) from frontmatter (metadata)
        """

        print("Parsing the markdown file")
        with open("blog.md") as f:
            _metadata, _content = frontmatter.parse(f.read())
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

        findfiles = FindFiles(self.owner_repo)

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
        """
        Dev.to publish
        """

        for file in self.parsedfiles:
            if file["metadata"]["publish_devto"]:
                if file["fileinfo"]["status"] == GITHUB_CODES.ADDED:
                    devto_create(metadata=self.metadata, content=self.content,
                                apikey=self.apikey, url=API_URLS.DEVTO)
                if file["fileinfo"]["status"] == GITHUB_CODES.MODIFIED:
                    # raise UpdationNotImplemented("dev.to")
                    devto_update()
            else:
                raise DidnotWantToPublish(
                    info="dev.to. publish_devto was set to false"
                )
