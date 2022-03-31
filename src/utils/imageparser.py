from bs4 import BeautifulSoup as BSHTML


def get_img_src(filename):
    """
    :return: imag src path parsed by Beautiful soup
    """

    with open(filename, 'r') as file:
        htmlText = file.read().replace('\n', '')
    soup = BSHTML(htmlText)
    images = soup.findAll('img')
    return images


def replace_with_url(filename, owner_repo, branch):
    """
    :return: replace the src in ima tag with github raw url
    """

    github_username_and_repo = owner_repo
    github_branch = branch
    image_list = get_img_src(filename)
    for relative_image_path in image_list:
        required_path = "media" + \
            relative_image_path['src'].split("media", 1)[1]
        url = f"https://raw.githubusercontent.com/{github_username_and_repo}/{github_branch}/{required_path}"
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(relative_image_path['src'], url)

        # Write the file out again
        with open(filename, 'w') as file:
            file.write(filedata)


def get_cover_image(cover_url, owner_repo, branch):
    """
    :param cover_url: frontmatter cover image url
    :return: cover image hosted github url
    """

    github_username_and_repo = owner_repo
    github_branch = branch
    required_path = "media" + cover_url.split("media", 1)[1]
    url = f"https://raw.githubusercontent.com/{github_username_and_repo}/{github_branch}/{required_path}"
    return url
