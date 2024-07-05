import supervision as sv


def draw_annotations(frame, detections, labels):
    box_annotator = sv.BoxAnnotator()

    # Format the labels based on the confidence values in the detections object
    formatted_labels = [
        f"{label} {confidence:0.2f}"
        for label, confidence in zip(labels, detections.confidence)
    ]

    annotated_frame = box_annotator.annotate(
        scene=frame.copy(),
        detections=detections,
        labels=formatted_labels
    )

    return annotated_frame