import cv2
from object_detector.model import load_grounding_dino_model
from object_detector.utils import draw_boxes


def detect_objects(model, frame, text_prompt, box_threshold, text_threshold):
    detections, labels = model.predict_with_caption(
        image=frame,
        caption=text_prompt,
        box_threshold=box_threshold,
        text_threshold=text_threshold
    )

    # Ensure that detections contain class_id
    if detections.class_id is None:
        detections.class_id = [0] * len(detections.xyxy)  # Assign a default class_id if missing

    annotated_frame = draw_boxes(frame.copy(), detections.xyxy, labels)

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

        try:
            # Detect objects in the frame
            annotated_frame = detect_objects(model, frame, text_prompt, box_threshold, text_threshold)

        except Exception as e:
            print(f"Error during object detection: {e}")
            continue

        if out is None:
            out = cv2.VideoWriter(output_video_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                                  (annotated_frame.shape[1], annotated_frame.shape[0]))

        out.write(annotated_frame)

    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()
