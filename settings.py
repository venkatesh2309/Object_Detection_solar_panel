# from pathlib import Path
# import sys

# # Get the absolute path of the current file
# file_path = Path(__file__).resolve()

# # Get the parent directory of the current file
# root_path = file_path.parent

# # Add the root path to the sys.path list if it is not already there
# if root_path not in sys.path:
#     sys.path.append(str(root_path))

# # Get the relative path of the root directory with respect to the current working directory
# ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'IMAGE'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, RTSP, YOUTUBE]

# Images config
# IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = r'C:\Users\venkatesh.g.lv\object_detect_streamlit\images\PV03_318198_1203939.BMP'
DEFAULT_DETECT_IMAGE = r'C:\Users\venkatesh.g.lv\object_detect_streamlit\predicted_Image\PV03_318198_1203939.BMP'


# ML Model config
#MODEL_DIR = ROOT / 'weights'
# DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
DETECTION_MODEL = r'C:\Users\venkatesh.g.lv\object_detect_streamlit\Model\best.pt'
# SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0
