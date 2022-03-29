import requests
from constants import GITHUB_CODES

# TODO:Use env variables for repository
# Assumption here is that user pushes a single commit each push


class FindFiles:
    """
    This class takes takes the big array of objects returned by GitHub api and 
    simplifies it to an list of dictionaries containing useful information
    """

    def __init__(self):
        self.latest_files = None
        self.data = {}
        self.useful_files = []

        self._latestCommitFiles()
        self._requiredFiles()
        print(f"List of dictionary to be processed : {self.useful_files}")

    def _latestCommitFiles(self):
        """
        A list of all the files related to the latest commit
        """

        all_commits = requests.get(
            "https://api.github.com/repos/aru31/test-blog-publish/commits")
        # getting sha of the latest commit
        latest_sha = all_commits.json()[0]["sha"]

        # getting the latest commit
        latest_commit = requests.get(
            f"https://api.github.com/repos/aru31/test-blog-publish/commits/{latest_sha}")
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
            if (file["status"] != GITHUB_CODES.REMOVED):
                get_file_name = file["filename"].split("/")

                # file should be a markdown hence should end with .md
                if(get_file_name[-1].split(".")[-1] == "md"):
                    '''
                    Download the markdown files only if they are in the blogs folder
                    Since there can be other md files in the repository and we only want to publish the ones
                    that are in the blogs folder or in its subfolder
                    '''
                    if(get_file_name[0] == "blogs"):
                        self.data["filename"] = get_file_name[-1]
                        self.data["url"] = file["raw_url"]
                        self.data["status"] = file["status"]

                        self.useful_files.append(self.data)


# c = FindFiles()
