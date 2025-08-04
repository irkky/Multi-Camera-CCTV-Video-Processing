# 🎥 Multi Camera CCTV Video Processing

<div align="center">

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

*A high-performance computer vision system for real-time person detection across multiple video feeds*

</div>

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 🔍 **Smart Detection**
- Real-time person detection using SSD MobileNet v2
- Configurable confidence threshold (default: 50%)
- Efficient TensorFlow Hub integration
- Optimized for performance

</td>
<td width="50%">

### ⚡ **High Performance**
- Multi-process parallel video processing
- Supports multiple video feeds simultaneously
- Grayscale output for reduced file size
- Configurable processing duration

</td>
</tr>
<tr>
<td width="50%">

### 🐳 **Docker Ready**
- Containerized deployment
- Minimal dependencies
- Easy scaling and distribution
- Production-ready configuration

</td>
<td width="50%">

### 📊 **Monitoring & Logging**
- Real-time FPS logging
- Comprehensive error handling
- Processing status updates
- Performance metrics

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker (optional)
- Video files or RTSP streams

### One-Command Setup

```bash
# Clone and run
git clone https://github.com/irkky/Multi-Camera-CCTV-Video-Processing
cd Multi-Camera-CCTV-Video-Processing
pip install -r requirements.txt
python app.py
```

### Docker Deployment

```bash
# Build and run with Docker
docker build -t video-processor .
docker run -v /path/to/videos:/app/videos video-processor
```

---

## 📦 Installation

<details>
<summary><b>🐍 Python Installation (Click to expand)</b></summary>

### 1. Clone the Repository
```bash
git clone https://github.com/irkky/Multi-Camera-CCTV-Video-Processing
cd multi-feed-video-processor
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install tensorflow tensorflow-hub
```

### 4. Verify Installation
```bash
python -c "import cv2, tensorflow as tf; print('✅ Installation successful!')"
```

</details>

<details>
<summary><b>🐳 Docker Installation (Click to expand)</b></summary>

### Build the Container
```bash
docker build -t video-processor .
```

### Run with Volume Mounting
```bash
docker run -v /host/path/videos:/app/videos \
           -v /host/path/output:/app/output \
           video-processor
```

</details>

---

## 🎯 Usage

### Basic Usage

```python
from app import process_multiple_feeds

# Define your video sources
video_files = [
    "/path/to/video1.mp4",
    "/path/to/video2.mp4",
    "rtsp://camera-ip:554/stream"  # RTSP streams supported
]

# Define output locations
output_files = [
    "/path/to/output1.mp4",
    "/path/to/output2.mp4",
    "/path/to/output3.mp4"
]

# Process all feeds in parallel
process_multiple_feeds(video_files, output_files)
```

### Single Feed Processing

```python
from app import process_video_feed

# Process a single video with custom duration
process_video_feed(
    video_file="input.mp4",
    output_file="output.mp4",
    duration=60  # Process for 60 seconds
)
```
---

## ⚙️ Configuration

### File Structure
```
multi-feed-video-processor/
├── 📄 app.py                 # Main application
├── 📄 requirements.txt       # Python dependencies
├── 🐳 dockerfile            # Docker configuration
├── 🧪 test_app.py           # Unit tests
├── 📁 videos/               # Input videos
├── 📁 output/               # Processed outputs
└── 📖 README.md
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest test_app.py -v

```

### Test Coverage

- ✅ Video feed processing
- ✅ Person detection accuracy
- ✅ Output file generation
- ✅ Error handling
- ✅ Multi-process execution

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🎯 Ways to Contribute

- **Bug Reports**: Found a bug? [Open an issue](../../issues)
- **Feature Requests**: Have an idea? [Start a discussion](../../discussions)
- **Code**: Submit a pull request

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

</div>
