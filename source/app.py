import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from azure.iot.device import IoTHubDeviceClient 
from azure.storage.blob import BlobServiceClient
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient as TextAnalyticsClientV3

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

connection_string = "HostName=sami-iothubdevice.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=FDCKTn9YcXOBjthIZTxcvr9lWPqYWvnl4JacS+aDskU="

parts = connection_string.split(";")
for part in parts:
    if part.startswith("HostName"):
        device_id = part.split("=")[1].split("-")[0]
        break

print("Device ID:", device_id)

# Set up Blob Storage Client
blob_conn_str = 'DefaultEndpointsProtocol=https;AccountName=mystorageaccount133;AccountKey=l5q20cWTta7JSOsDvtjn3RJJxzveqndPp0ONJ3mt2UyeXMzhCVp93F9LXU7JJkHSDTNa99wbn/Ay+AStpL6PYg==;EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)

# Set up Text Analytics Client
text_analytics_key = '4f5f3623e2eb4e8a85802b78e7d1352c'
text_analytics_endpoint = 'https://sami-textanalytics.cognitiveservices.azure.com/'
text_analytics_client = TextAnalyticsClient(text_analytics_endpoint, AzureKeyCredential(text_analytics_key))

# Set up Text Analytics V3 Client
text_analytics_v3_key = '4f5f3623e2eb4e8a85802b78e7d1352c'
text_analytics_v3_endpoint = 'https://sami-textanalytics.cognitiveservices.azure.com/'
text_analytics_v3_client = TextAnalyticsClientV3(endpoint=text_analytics_v3_endpoint, credential=AzureKeyCredential(text_analytics_v3_key))

# Define your routes and implement the necessary functionality
@app.route('/calculate-carbon-footprint', methods=['POST'])
def calculate_carbon_footprint():
    # Retrieve user inputs from request
    software_name = request.json.get('software_name')
    programming_language = request.json.get('programming_language')
    lines_of_code = request.json.get('lines_of_code')
    deployment_environment = request.json.get('deployment_environment')
    num_users = request.json.get('num_users')

    # Validate the input fields
    if not all([software_name, programming_language, lines_of_code, deployment_environment, num_users]):
        return jsonify({'error': 'Invalid input data'}), 400

    # Perform more advanced calculations for the carbon footprint
    carbon_footprint = lines_of_code * 0.1 + num_users * 2

    # Enhance integration with Azure services
    # Trigger actions based on the calculated carbon footprint using Azure Functions or Logic Apps
    
    function_app_url = 'https://sami-functionapp.azurewebsites.net/api/HttpTrigger1?code=3wD-bKpO-JB4GXAsgKbGpDuSAyTh0-cn8yzoiHlYks6jAzFut7bVlA=='

    # Trigger the Azure Function
    response = requests.post(function_app_url, json={'data': 'your-data'})

    # Check the response from the Azure Function
    if response.status_code == 200:
        # Handle the successful response
        print('Azure Function triggered successfully')
    else:
        # Handle the error response
        print('Error triggering Azure Function:', response.status_code)

    # Integrate with Microsoft Sustainability Manager or other sustainability frameworks
    # to provide comprehensive sustainability insights and recommendations based on the carbon footprint

    # Implement authentication and authorization mechanisms
    # Secure the API endpoints and ensure only authorized clients can access the functionality

    # Add logging and monitoring capabilities
    # Track API usage, errors, and performance metrics

    # Implement unit tests
    # Verify the correctness of calculations and functionality of API endpoints

    # Return the carbon footprint and insights as a response
    result = {
        'carbon_footprint': carbon_footprint,
        'insights': ['Insight 1', 'Insight 2']
    }

    return jsonify(result), 200


# Define additional routes
@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Carbon Footprint API'

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return 'Favicon'


if __name__ == '__main__':
    app.run(debug=True)
