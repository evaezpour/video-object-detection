from video_object_detection.video_processor import process_video


def main():
    input_video_path = './input_video/street_trim.mp4'
    output_video_path = './output_video/output_video.mp4'
    text_prompt = 'all flowers'

    process_video(input_video_path, output_video_path, text_prompt)


if __name__ == '__main__':
    main()
