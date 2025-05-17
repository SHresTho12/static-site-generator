from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    CODE = "code"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"
    HEADING = "heading"
    HORIZONTAL_RULE = "horizontal_rule"
    DIVIDER = "divider"
    TABLE = "table"

class BlockTags(Enum):
    PARAGRAPH = "p"
    QUOTE = "blockquote"
    CODE = "code"
    ORDERED_LIST = "ol"
    UNORDERED_LIST = "ul"
    HEADING = "h1"
    HORIZONTAL_RULE = "hr"
    DIVIDER = "br"
    TABLE = "table"   


def block_to_block_type(block):
    if not block:
        return BlockType.PARAGRAPH
    if re.match(r"^#{1,6} ",block):
        return BlockType.HEADING
    if re.match(r"^`{3}",block) and re.search(r"`{3}$",block):
        return BlockType.CODE
    lines = block.splitlines()

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(re.match(r"^-\s", line) for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(rf"^{i+1}\.\s", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST    
    return BlockType.PARAGRAPH
