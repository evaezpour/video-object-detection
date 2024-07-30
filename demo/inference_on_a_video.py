from object_detector.video_processor import process_video

input_video_path = "./input_video/street_trim.mp4"
output_video_path = "./output_video/street_trim_people.mp4"
text_prompt = "people"

process_video(input_video_path, output_video_path, text_prompt)

