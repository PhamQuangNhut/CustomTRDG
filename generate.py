from trdg.data_generator import FakeTextDataGenerator
from tqdm import tqdm
import os
import config
import utils
import random
save_data = []
if __name__ == "__main__" :
     with open(config.CORPUS_PATH, 'r', encoding='utf-8') as file:
          lines = file.readlines() 
     paragraphs = []
     for line in lines:
          paragraphs.extend(line.split('\n'))
     paragraphs = [paragraph for paragraph in paragraphs if paragraph.strip()]
     paragraphs = set(paragraphs) #Lọc những nội dung bị trùng
     if not os.path.exists(config.OUTPUT_PATH) :
          os.makedirs(config.OUTPUT_PATH)
     for i, text in tqdm(enumerate(paragraphs)) :
          font = utils.get_random_font(config.FONT_PATH)
          alignment = random.randint(config.ALIGNMENT_MIN, config.ALIGNMENT_MAX)
          space_width = random.randint(config.SPACE_WIDTH_MIN, config.SPACE_WIDTH_MAX)
          character_spacing = random.randint(config.SPACING_MIN, config.SPACING_MAX)

     # Sử dụng hàm để tạo một biến chứa màu ngẫu nhiên
          text_color = utils.generate_random_color()
          random_elements = tuple(random.randint(config.MARGIN_MIN, config.MARGIN_MAX) for _ in range(4))
          margins = (5, 5, 5, 5)[:-len(random_elements)] + random_elements
          fit = bool(random.getrandbits(1)) 
          background_type = random.randint(0, 1)
          size = random.randint(config.SIZE_MIN, config.SIZE_MAX)
          blur = random.randint(config.BLUR_MIN, config.BLUR_MAX)
          print(text)
          FakeTextDataGenerator.generate(
               index = i,
               text = text,
               font =font,
               out_dir = config.OUTPUT_PATH,
               size =size,
               extension = 'jpg',
               skewing_angle = 3,
               random_skew = True,
               blur =blur,
               random_blur = True,
               background_type =background_type,
               distorsion_type = 0,
               distorsion_orientation = 0,
               is_handwritten = False,
               width = -1,
               alignment =alignment,
               text_color = text_color,
               orientation = 0,
               space_width =space_width,
               character_spacing =character_spacing,
               margins =margins,
               fit =fit,
               output_mask = False,
               word_split =  False,
               image_dir = '',
               name_format = 2,
               )
     save_data.append({
          'text': utils.post_process(text),
          'image_name': f'{i}.jpg'  # Assuming you use index 'i' for image filenames
     })
