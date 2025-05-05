def markdown_to_blocks(markdown):
    if not markdown:
        return []
    

    raw_blocks = markdown.strip().split("\n\n")

    clean_blocks = []
    for block in raw_blocks:
        # Strip each line in the block
        lines = [line.strip() for line in block.strip().splitlines()]
        cleaned_block = "\n".join(lines).strip()
        
        if cleaned_block:  
            clean_blocks.append(cleaned_block)

    return clean_blocks
