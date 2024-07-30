import cv2
import random


def get_random_color():
    """
    Generate a random color in BGR format.
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_boxes(frame, boxes, labels):

    colors = [get_random_color() for _ in range(len(boxes))]  # Generate random colors for each box

    for i, (box, label) in enumerate(zip(boxes, labels)):
        # Extract the coordinates and color
        x1, y1, x2, y2 = box
        color = colors[i]  # Use the color for this box

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame
