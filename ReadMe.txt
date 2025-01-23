Celebrity Classifier
This project is a machine learning-based celebrity image classifier built using Flask, OpenCV, and wavelet transformation techniques. It classifies images of celebrities based on their faces using a pre-trained machine learning model. The classifier detects faces in the provided images, extracts features using wavelet decomposition, and then predicts the celebrity class.


Features:
Image Classification: Classifies celebrity images by detecting faces and applying wavelet transformation for feature extraction.
Face Detection: Uses Haar cascade classifiers to detect faces and eyes in the provided image, cropping the region of interest (ROI) for better analysis.
Wavelet Transform: The images undergo a wavelet transform to highlight high-frequency features like edges, enhancing the model's ability to classify images accurately.
API Interface: A RESTful API using Flask for easy image classification with base64-encoded image data.
Cross-Origin Resource Sharing (CORS): The API supports CORS, enabling it to interact with frontend applications hosted on different domains.


