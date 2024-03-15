import random
import os
import matplotlib.colors as mcolors
import jaconv, re

def generate_random_color():
    # Danh sách các màu cơ bản (đỏ, đen, xanh) và variation đậm, nhạt của chúng
    base_colors = ['#FF0000', '#000000', '#0000FF']  # Đỏ, đen, xanh
    variations = [0.2, 0.4, 0.6, 0.8]  # Variation: 20%, 40%, 60%, 80%

    # Chọn một màu cơ bản ngẫu nhiên
    base_color = random.choice(base_colors)

    # Tạo biến thể đậm hoặc nhạt
    variation = random.choice(variations)
    rgb_color = mcolors.to_rgb(base_color)
    new_color = mcolors.to_hex([min(1, c * variation) for c in rgb_color])

    return new_color

def get_random_font(font_path) :

# Lấy danh sách các tệp tin trong thư mục
  files_list = os.listdir(font_path)

# Chọn ngẫu nhiên một tệp tin từ danh sách
  random_file = random.choice(files_list)
  return os.path.join(font_path, random_file)

def post_process(text):
    text = ''.join(text.split())
    text = text.replace('…', '...')
    text = re.sub('[・.]{2,}', lambda x: (x.end() - x.start()) * '.', text)
    text = jaconv.h2z(text, ascii=True, digit=True)
    return text