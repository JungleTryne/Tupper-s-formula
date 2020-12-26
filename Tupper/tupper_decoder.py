from PIL import Image, ImageDraw

from Tupper.tupper_constants import IMAGE_MODE, WIDTH, HEIGHT, \
    AREA, SIZE_TUPLE, DEFAULT_IMAGE_COLOR

class TupperDecoder:
    def _height_to_bin(self, height: int) -> str:
        """
        This is the first step of reverse Tupper's algo
        We take the height (mentioned as 'k' in the article)
        and convert it into binary form after dividing it by 17

        :param: height - Height of the image
        :return: String of binary form
        """

        height //= 17

        bin_tail = bin(height)[2:]
        remain = (AREA - len(bin_tail))
        binary = ('0' * remain) + bin_tail

        return binary

    def _bin_to_image_lists(self, binary: str) -> list:
        """
        This is the second step of revers Tupper's algo
        We look at the binary form of the image height and try
        to decode it.

        :param: binary - Binary form of the height
        :return: Image form of lists
        """

        image_lists = [list() for x in range(HEIGHT)]

        for i in range(AREA):
            current_row = -(i % HEIGHT)
            image_lists[current_row].append(binary[i])

        return image_lists
    

    def generate_image(self, height: int) -> Image:
        """
        This method generates image from its height using
        Tupper's formula

        :param: height - Image height
        :return: PIL image object
        """

        binary = self._height_to_bin(height)
        image_lists = self._bin_to_image_lists(binary)

        image = Image.new(
            IMAGE_MODE, 
            SIZE_TUPLE, 
            DEFAULT_IMAGE_COLOR
        )

        for y in range(HEIGHT):
            for x in range(WIDTH):
                pixel_value = (int(image_lists[y][x],))

                image.putpixel(
                    xy=(WIDTH - x - 1, -y),
                    value=pixel_value
                )

        return image
