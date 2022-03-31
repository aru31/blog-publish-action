class WebsiteNotSupported(Exception):
    def __init__(self, info=""):
        message = f'Website Not Supported {info}'
        super().__init__(message)


class IndexException(Exception):
    def __init__(self, info=""):
        message = f'Not all arguments provided, expected arguments are {info}'
        super().__init__(message)


class WrongURLException(Exception):
    def __init__(self, info=""):
        message = f'The markdown file couldnot be downloaded may be the URL is wrong, URL:  {info}'
        super().__init__(message)


class MissingFrontmatterException(Exception):
    def __init__(self, info=""):
        message = f'Some frontmatter field is missing, refer readme to know more  {info}'
        super().__init__(message)
