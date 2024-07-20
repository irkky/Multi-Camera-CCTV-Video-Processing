import cv2
import numpy as np
import multiprocessing as mp
import time
import logging
import os
import tensorflow as tf
import tensorflow_hub as hub

# Configure logging
logging.basicConfig(level=logging.INFO)

# Loading the pre-trained model
MODEL_URL = "https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2"
detector = hub.load(MODEL_URL)

def detect_persons(frame):
    # Convert frame to tensor
    tensor = tf.convert_to_tensor(frame)
    tensor = tensor[tf.newaxis, ...]

    # Performing detection
    result = detector(tensor)
    result = {key: value.numpy() for key, value in result.items()}

    # Extracting detection results
    detection_classes = result["detection_classes"]
    detection_scores = result["detection_scores"]
    detection_boxes = result["detection_boxes"]

    # Filter results for person class
    person_detections = []
    for i in range(detection_classes.shape[1]):  # Assuming the second dimension represents detections
        if detection_classes[0, i] == 1 and detection_scores[0, i] >= 0.5:
            box = detection_boxes[0, i]
            person_detections.append(box)

    return person_detections

# Function to simulate video feed ingestion and processing
def process_video_feed(video_file, output_file, duration=2000):
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        logging.error(f"Failed to open video file {video_file}")
        return

    # Define the codec and create VideoWriter object for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))), False)
    
    if not out.isOpened():
        logging.error(f"Failed to open output file {output_file}")
        return

    start_time = time.time()
    while cap.isOpened() and (time.time() - start_time < duration):
        ret, frame = cap.read()
        if not ret:
            break

        # Detecting persons
        person_detections = detect_persons(frame)

        # Draw bounding boxes
        for box in person_detections:
            y1, x1, y2, x2 = box
            x1, y1, x2, y2 = int(x1 * frame.shape[1]), int(y1 * frame.shape[0]), int(x2 * frame.shape[1]), int(y2 * frame.shape[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Converting to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Writing the frame
        out.write(gray_frame)

        # Log FPS
        fps = cap.get(cv2.CAP_PROP_FPS)
        logging.info(f"Processing {video_file} at {fps} FPS")

    cap.release()
    out.release()
    logging.info(f"Finished processing {video_file}")

# Function to handle multiple video feeds in parallel
def process_multiple_feeds(video_files, output_files):
    processes = []
    for video_file, output_file in zip(video_files, output_files):
        p = mp.Process(target=process_video_feed, args=(video_file, output_file))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    # Placeholder video files (replace with actual RTSP URLs or video file paths)
    video_files = [
        "D:/Computer vision/videos/video1.mp4",
        "D:/Computer vision/videos/video2.mp4",
        "D:/Computer vision/videos/video3.mp4"
    ]
    
    # Output files (specify where you want to save the processed videos)
    output_files = [
        "D:/Computer vision/output/output1.mp4",
        "D:/Computer vision/output/output2.mp4",
        "D:/Computer vision/output/output3.mp4"
    ]

    # Ensure output directory exists
    output_dir = "D:/Computer vision/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process_multiple_feeds(video_files, output_files)
