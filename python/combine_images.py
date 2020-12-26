import sys
from PIL import Image

# images = [Image.open(x) for x in ['colossus_run_001.png', 'colossus_run_002.png', 'colossus_run_003.png', 'colossus_run_004.png', 'colossus_run_005.png', 'colossus_run_006.png']]
# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('colossus.png')

# im1 = Image.open("colossus_run_001.png")
# im2 = Image.open("colossus_run_002.png")
# blended = Image.blend(im1, im2, alpha=0.5)
# blended.save("blended.png")


background = Image.open("stage_02.png")
foreground = Image.open("colossus_run_001.png")

background.paste(foreground, (0, 0), None)
background.save("merged.png")
background.show()