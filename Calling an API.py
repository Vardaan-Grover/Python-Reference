#DOCUMENTATION LINK
#https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-ga/operations/56f91f2e778daf14a499f21b

#Use the requests library to simplify making a REST API call from Python
import requests 


#We will need the JSON library to read the data passed back by the web service
import json

#We need the key to access our Computer Vision Service/API
SUBSCRIPTION_KEY = '68fab62c201a4aa9891215a3603f3f36'

#Address of our Computer Vision Service
vision_service_address_ENDPOINT = 'https://pythoncomputervisionapivardaan.cognitiveservices.azure.com/vision/v3.0/'

#Add the the format of the function that you want to call to the above address after referring it from the respective(Cognitive Services Documentation) Documentation
ADDRESS = vision_service_address_ENDPOINT+'analyze'

#According the documentation for the analyze function
#There are 3 optional parameters: visualFeatures, details and language
parameters = {'visualFeatures': 'Description, Faces,  Color', 'language':'en'}

#Open an image file to get the file object to analyze
image_path = 'C:/Users/coolv/Documents/Niya.jpg'
image_data = open(image_path, 'rb').read()

#According to the documentation of the analyze image function we need to specify the subscription key and the content type in the HTTP header
#Content-Type is application/octet-stream. Refer from the documentation.
headers = {'Content-Type':'application/octet-stream', 'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY}

#We will use the HTTP POST to call this function/API
response = requests.post(ADDRESS, headers=headers, params=parameters, data=image_data)

#This will raise an exception if the above call raises an error
response.raise_for_status()

#Response that has been given by the server where the our POST call had gone is mostly in the form of JSON
#Displaying the JSON results that have been returned
results = response.json()
print(json.dumps(results))