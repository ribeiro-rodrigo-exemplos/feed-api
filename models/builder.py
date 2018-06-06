
class TextBlockBuilder:

    def __init__(self, html_helper):
        self.__html_helper = html_helper

    def build(self, tree):
        paragraphs = tree.findall('.//p')
        paragraphs = [self.__html_helper.extract_text(p) for p in paragraphs if
                      len(p.text.strip()) != 0 or len(p.getchildren()) > 0]
        blocks = [{'type': 'text', 'content': p} for p in paragraphs]

        return blocks


class ImageBlockBuilder:
    def build(self, tree):
        images = tree.findall('.//div//img')
        blocks = [{'type': 'image', 'content': img.get('src')} for img in images]
        return blocks


class LinksBlockBuilder:
    def build(self, tree):
        uls = tree.findall('.//div//ul')
        blocks = []
        for ul in uls:
            links = [l.get('href') for l in ul.findall('.//li/a')]
            blocks.append({'type': 'links', 'content': links})

        return blocks
