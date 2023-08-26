import time
def format_flossart(string: str):
    pass


def update_glossary():
    pass


def temp_gen():
    with open("src/temp.txt") as f:
        for line in f:
            yield line

gen = temp_gen()
def chat_with_gpt(string: str) -> str:
    """run each time user sends a message"""
    return next(gen)

def init(str):
    """should run this when user enters conv"""
    time.sleep(2)
    return """mock start message
    This shoudl be on new line
    and this
    """

def end(msg, path_to_json):
    """should run this when user leaves conv
    when uesr clck end button"""
    time.sleep(2)
    return """mock end message"""

