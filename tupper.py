import argparse
import traceback

from Tupper.tupper_encoder import TupperEncoder
from Tupper.tupper_decoder import TupperDecoder


def print_help():
    help_message = \
    '''
    Usage: python3 tupper.py -e habr.png -o height.txt
    '''

    print(help_message)


def encode(input_path, output_path):
    encoder = TupperEncoder()
    result = encoder.get_height(input_path)
    
    if not output_path:
        print("result: {0}".format(result))
        return

    with open(output_path, 'w+') as f:
        f.write(str(result)) 


def decode(input_path, output_path):
    decoder = TupperDecoder()

    height = None
    with open(input_path, 'r') as f:
        height = int(f.read())

    image = decoder.generate_image(height)
    output_path = 'output.png' if output_path is None else output_path
    image.save(output_path)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--encode", help="Encode image to Tupper's height")
    parser.add_argument("-d", "--decode", help="Decode Tupper's height to image")
    parser.add_argument("-o", "--output", help="Output path of the result of the \
        certain scenario")

    args = parser.parse_args()

    try:
        if args.encode:
            input_path = args.encode
            output_path = args.output
            encode(input_path, output_path)

        elif args.decode:
            input_path = args.decode
            output_path = args.output
            decode(input_path, output_path)
        else:
            print_help()
        
    except Exception as e:
        print("Caught Exception: {0}".format(traceback.format_exc()))
        print_help()

if __name__ == '__main__':
    main()
