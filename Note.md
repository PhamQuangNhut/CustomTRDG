TRDG is bugging. To run you have to fix the code 
File "D:\anaconda3\envs\TrOCR\lib\site-packages\trdg\utils.py", line 122, in get_text_height
FROM : 
def get_text_height(image_font, text):
    """
    Get the width of a string when rendered with a given font
    """
    return image_font.getsize(text)[1]
TO : 
def get_text_height(image_font, text: str) -> int:
    """
    Get the height of a string when rendered with a given font
    """
    left, top, right, bottom = image_font.getbbox(text)
    return bottom
