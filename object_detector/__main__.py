from object_detector.video_processor import process_video
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_video_path", type=str, required=True)
parser.add_argument("-o", "--output_video_path", type=str, required=True)
parser.add_argument("-t", "--text_prompt", type=str, required=True)
args = parser.parse_args()


def main():
    input_video_path = args.input_video_path
    output_video_path = args.output_video_path
    text_prompt = args.text_prompt

    process_video(input_video_path, output_video_path, text_prompt)


if __name__ == '__main__':
    main()
