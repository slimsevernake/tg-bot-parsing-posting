from pydantic import BaseModel
import parser

class Site(BaseModel):
    url: str
    container_tag: str
    container_class: str
    block_tag: str
    block_class: str
    block_link: str
    block_text: str
    time_format: list[str, str]

    def get_today_articles(self):
        return parser.main_page_parse(self)
