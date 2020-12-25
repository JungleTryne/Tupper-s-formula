from PIL import Image, ImageDraw

from Tupper.tupper_constants import IMAGE_MODE, WIDTH, HEIGHT, \
    AREA, SIZE_TUPLE, TWO_COLOR_MODE, BLACK_COLOR_CODE


class TupperEncoder:
    def get_height(self, image_path: str) -> int:
        """
        This method return code of the image using
        Tupper's formula

        :param: image_path - Path of the image
        :return: Tupper's height 
        """

        image = Image.open(image_path)

        height, width = image.size
        if width == WIDTH and height == HEIGHT:
            raise Exception("Wrong size. Must be {0}x{1}".format(WIDTH, HEIGHT))

        image = image.convert(TWO_COLOR_MODE)
        binary = str()

        for x in range(WIDTH - 1, -1, -1):
            for y in range(HEIGHT):
                binary += '1' if image.getpixel((x, y)) > BLACK_COLOR_CODE else '0'

        height = int(binary, 2) * 17
        return height
