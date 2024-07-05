from supervision.detection.annotate import BoundingBoxAnnotator, LabelAnnotator


def draw_annotations(frame, detections, labels):
    bounding_box_annotator = BoundingBoxAnnotator()
    label_annotator = LabelAnnotator()

    # Format the labels based on the confidence values in the detections object
    formatted_labels = [
        f"{label} {confidence:0.2f}"
        for label, confidence in zip(labels, detections.confidence)
    ]

    annotated_frame = frame.copy()
    annotated_frame = bounding_box_annotator.annotate(scene=annotated_frame, detections=detections)
    annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections, labels=formatted_labels)

    return annotated_frame