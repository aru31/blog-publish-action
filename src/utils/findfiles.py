import requests
from constants.constants import *

# Assumption here is that user pushes a single commit each push


class FindFiles:
    """
    This class takes takes the big array of objects returned by GitHub api and 
    simplifies it to an list of dictionaries containing useful information
    """

    def __init__(self, owner_repo, logger):
        self.logger = logger
        self.owner_repo = owner_repo
        self.latest_files = None
        self.files_changed = []
        self.data = {}
        self.useful_files = []

        self.logger.info("Processing the files")
        self._latestCommitFiles()
        self._requiredFiles()
        self.logger.debug(
            f"List of file names that changed : {self.files_changed}")
        self.logger.info(
            f"List of dictionary of files to be processed : {self.useful_files}")

    def _latestCommitFiles(self):
        """
        A list of all the files related to the latest commit
        """

        all_commits = requests.get(
            f"{API_URLS.GITHUB}/{self.owner_repo}/commits")
        # getting sha of the latest commit
        latest_sha = all_commits.json()[0]["sha"]

        # getting the latest commit
        latest_commit = requests.get(
            f"{API_URLS.GITHUB}/{self.owner_repo}/commits/{latest_sha}")

        # for for local testing, this commit contains files that were renamed, modified and removed
        # latest_commit = requests.get(
        #     "https://api.github.com/repos/aru31/test-blog-publish/commits/fab6b1b208433e4f52dd21afd747e2b629bb432c")

        # for for local testing, this commit contains files that were renamed, modified and added
        # latest_commit = requests.get(
        #     "https://api.github.com/repos/aru31/test-blog-publish/commits/616a26b4f5458f02943113b2ef33149de8db4e62")

        latest_files = latest_commit.json()["files"]
        self.latest_files = latest_files

    def _requiredFiles(self):
        """
        List of dictionary of all the files that we are going to process 
        sample: [
            {
             "filename": "hello.md",
             "raw_url": "http://...",
             "status": "..." 
             }
        ]
        """
        for file in self.latest_files:
            self.files_changed.append(file["filename"])

            # only process files that have status of created
            if (file["status"] == GITHUB_CODES.ADDED or file["status"] == GITHUB_CODES.RENAMED):
                """
                Expected patterns of file["filename"]:
                blogs/blog.md
                blogs/../blog.md
                Readme.md
                someotherfile
                otherfolder/file
                """
                get_file_name = file["filename"].split("/")
                # file should be a markdown hence should end with .md
                if(get_file_name[-1].split(".")[-1] == "md"):
                    '''
                    Download the markdown files only if they are in the blogs folder
                    Since there can be other md files in the repository and we only want to publish the ones
                    that are in the blogs folder or in its subfolder
                    '''
                    if(get_file_name[0] == CONSTANTS.FOLDER_NAME):
                        self.data = dict()
                        self.data["filename"] = get_file_name[-1]
                        self.data["url"] = file["raw_url"]
                        self.data["status"] = file["status"]

                        self.useful_files.append(self.data)
