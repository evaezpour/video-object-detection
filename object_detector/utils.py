import supervision as sv


def draw_annotations(frame, detections, labels):
    box_annotator = sv.BoxAnnotator()

    '''
    formatted_labels = [
        f"{label} {confidence:0.2f}"
        for label, (_, confidence, class_id, _)
        in zip(labels, detections)
    ]
    annotated_frame = box_annotator.annotate(scene=frame.copy(), detections=detections, labels=formatted_labels)
    '''

    # Adjust the unpacking based on actual detection structure
    try:
        formatted_labels = [
            f"{label} {confidence:0.2f}"
            for label, (_, confidence, class_id, _)
            in zip(labels, detections)
        ]
    except ValueError as e:
        print(f"ValueError: {e}")
        formatted_labels = [
            f"{label} {detection[1]:0.2f}"
            for label, detection in zip(labels, detections)
        ]

    annotated_frame = box_annotator.annotate(scene=frame.copy(), detections=detections, labels=formatted_labels)

    return annotated_frame
