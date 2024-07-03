import cv2
from video_object_detection.model import load_grounding_dino_model
from video_object_detection.utils import draw_annotations


def detect_objects(model, frame, text_prompt, box_threshold, text_threshold):
    detections, labels = model.predict_with_caption(
        image=frame,
        caption=text_prompt,
        box_threshold=box_threshold,
        text_threshold=text_threshold
    )
    return detections, labels


def process_frame(model, frame, text_prompt, box_threshold, text_threshold):
    detections, labels = detect_objects(model, frame, text_prompt, box_threshold, text_threshold)
    print(labels)
    annotated_frame = draw_annotations(frame, detections, labels)
    return annotated_frame


def process_video(input_video_path, output_video_path, text_prompt, box_threshold=0.35, text_threshold=0.25):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = None

    model = load_grounding_dino_model()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        annotated_frame = process_frame(model, frame, text_prompt, box_threshold, text_threshold)

        if out is None:
            out = cv2.VideoWriter(output_video_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                                  (annotated_frame.shape[1], annotated_frame.shape[0]))

        out.write(annotated_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
