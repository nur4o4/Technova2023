#need to pip install google-search-results and google-reverse-search
from serpapi import GoogleSearch

params = {
  "api_key": "cda799d2356be09a2791b316a49a992324c7d05b07b443e4b9eab7134ceb8075",
  "engine": "google_reverse_image",
  "google_domain": "google.com",
  "image_url": "https://i.imgur.com/HBrB8p0.png"
}

search = GoogleSearch(params)
results = search.get_dict()

image_results = results['inline_images']

for image_result in image_results:
  print(image_result["source"])

# from deepface import DeepFace

# models = [
#   "VGG-Face",
#   "Facenet",
#   "Facenet512",
#   "OpenFace",
#   "DeepFace",
#   "DeepID",
#   "ArcFace",
#   "Dlib",
#   "SFace",
# ]

# result = DeepFace.verify(img1_path = "Taylor 1.jpg",
#       img2_path = "Justin.jpg",
#       model_name = models[0]
# )
# print(result['verified'])
