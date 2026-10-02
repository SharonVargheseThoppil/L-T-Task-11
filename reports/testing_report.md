# Task 11: Full Application Containerization

## Testing Report

### Project Overview

**Project Title:** Full Application Containerization of a Deep Learning Solution

**Technology Stack:** Python, TensorFlow, Flask, Streamlit, Docker, Docker Compose

**Dataset:** CIFAR-10

**Application Type:** Image Classification

### Objective

The objective of this task is to containerize a complete deep learning solution consisting of a trained CNN model, Flask REST API, and Streamlit user interface. The application integrates these components using Docker and Docker Compose to provide an environment for image classification, API communication, and deployment testing.

### Testing Environment

* Operating System: Windows
* Container Platform: Docker Desktop
* Backend: Flask
* Frontend: Streamlit
* Deep Learning Framework: TensorFlow
* Container Orchestration: Docker Compose
* Model Architecture: Convolutional Neural Network (CNN)
* Dataset: CIFAR-10
* Flask API Port: 5000
* Streamlit UI Port: 8501

### Test Cases

| Test ID | Test Case                    | Expected Result           | Actual Result                                                                                                                                                     | Status |
| ------- | ---------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| TC01    | Docker version check         | Docker available          | Docker commands executed successfully during the implementation.                                                                                                  | Passed |
| TC02    | Docker Compose validation    | Configuration valid       | `docker compose config` and `docker compose config --services` validated the configuration, and it was used successfully to build and run the application services. | Passed |
| TC03    | Docker image build           | Images build successfully | Flask API and Streamlit UI Docker images were built successfully.                                                                                                 | Passed |
| TC04    | Container startup            | Both services start       | Both application containers were observed running. An earlier UI restart was followed by a healthy state.                                                         | Passed |
| TC05    | Flask home endpoint          | HTTP 200                  | The Flask home endpoint returned application information and available API endpoints.                                                                             | Passed |
| TC06    | Model health check           | Model loaded              | The health endpoint reported a healthy status and confirmed that the model was loaded.                                                                            | Passed |
| TC07    | Valid image upload           | Prediction JSON returned  | An image prediction was successfully generated, with the predicted class displayed as Dog and confidence of 94.41%.                                               | Passed |
| TC08    | Missing image request        | HTTP 400                  | The API returned the expected missing-image validation response.                                                                                                  | Passed |
| TC09    | Streamlit UI access          | Interface loads           | The Streamlit application was accessible at port 8501 and displayed the image classification interface.                                                           | Passed |
| TC10    | Frontend-backend integration | Prediction displayed      | The uploaded image was processed through the Flask API, and the prediction result was displayed in Streamlit.                                                     | Passed |
| TC11    | Container restart            | Services restart          | `docker compose restart` restarted both containers. `docker compose ps` then showed both running and healthy, and the health endpoint and Streamlit UI responded normally afterwards. | Passed |
| TC12    | Docker network inspection    | Services connected        | `docker network inspect` showed both containers on the Compose default network, and the Streamlit container reached the Flask health endpoint at `http://flask-api:5000`. | Passed |

### Model Training and Evaluation Results

The CIFAR-10 CNN model was trained and evaluated before being packaged into the Dockerized application.

The training output showed the following results:

| Evaluation Metric         | Observed Result |
| ------------------------- | --------------: |
| Number of Training Epochs |               5 |
| Training Accuracy         |          68.44% |
| Validation Accuracy       |          68.60% |
| Test Accuracy             |          67.62% |
| Test Loss                 |          0.9235 |
| Model Saving              |      Successful |

The trained model was saved successfully and used by the Flask API for image classification.

### Docker Deployment Results

The Docker build process completed successfully for both application components.

| Component           | Configuration       | Observed Result           |
| ------------------- | ------------------- | ------------------------- |
| Flask API           | Port 5000           | Container running         |
| Streamlit UI        | Port 8501           | Container running         |
| Flask API Health    | Docker health check | Healthy                   |
| Streamlit UI Health | Docker health check | Healthy                   |
| Model Integration   | TensorFlow CNN      | Model loaded successfully |

The final container status screenshot demonstrated that both services reached a healthy state.

### API Testing Results

The Flask API was tested using its available endpoints.

**Home Endpoint:**

The API returned information about the application and its available endpoints.

**Health Endpoint:**

The API reported a healthy status and confirmed successful model loading. The endpoint was queried from the host and again after the container restart, with the same result.

**Prediction Endpoint:**

A valid image was uploaded and processed successfully. The API returned a prediction result that was also displayed in the Streamlit interface.

**Invalid Request:**

A request without an image was tested, and the API returned the expected validation error.

### Container Restart and Network Verification

**Container Restart Test:**

Both services were restarted using `docker compose restart`. After the restart, `docker compose ps` showed both containers running with a healthy status. The Flask health endpoint still reported the model as loaded, and the Streamlit interface loaded normally at port 8501.

**Docker Network Inspection:**

`docker network ls` and `docker network inspect` showed that both containers were attached to the Compose default network, each with its own IP address on the same subnet.

**Inter-Container Communication:**

The Flask health endpoint was queried from the host and then from inside the Streamlit container using the service name `flask-api` on the internal Docker network. Both requests returned `model_loaded: true` and `status: healthy`.

### Automated Unit Tests

Unit tests for the health endpoint and the missing-image request were run with the `unittest` framework. Both tests completed with an OK result.

### Observations

1. The complete application was organized into separate model, API, and UI components.
2. The CIFAR-10 CNN model was trained, evaluated, and saved successfully.
3. Docker images for the Flask API and Streamlit UI were built successfully.
4. Docker Compose was used to run the application services.
5. The Flask API successfully loaded the trained model and processed image prediction requests.
6. The Streamlit interface successfully communicated with the Flask backend and displayed the prediction output.
7. The observed prediction was **Dog with 94.41% confidence**.
8. Both application containers were subsequently observed in a healthy state.
9. An earlier Streamlit container restart was observed before the later healthy status.
10. A container restart test was performed, and both containers returned to a running and healthy state.
11. Docker network inspection showed both containers on the same Compose network, and the Streamlit container reached the Flask API by service name.
12. The automated unit tests for the health endpoint and the missing-image request passed.

### Results

The implementation demonstrated successful model training, Docker image creation, container startup, container restart, Flask API operation, model loading, image prediction, Docker network connectivity, and Streamlit integration.

The final observed Docker status showed both the Flask API and Streamlit UI containers running with healthy status.

The application successfully processed an uploaded image and displayed the predicted class and confidence score through the user interface.

The model achieved a test accuracy of 67.62% during the recorded evaluation.

### Conclusion

The Task 11 implementation successfully demonstrated the containerization and integration of a complete deep learning application consisting of a CNN model, Flask REST API, and Streamlit user interface.

Docker and Docker Compose were used to package and run the application components. The successful API responses, model health check, container status, restart test, network verification, and image prediction results demonstrate the functionality of the integrated solution.

The application achieved the intended core functionality of accepting an image, performing deep learning inference, and displaying the prediction through the Streamlit interface.

The implementation therefore demonstrates successful completion of the core technical objectives of Full Application Containerization. The architecture documentation, testing evidence, and final submission packaging should be maintained as supporting deliverables.

### Limitations

* The classifier is designed for the ten categories included in the CIFAR-10 dataset.
* Prediction confidence does not guarantee that the predicted class is correct.
* The observed test accuracy was 67.62%, indicating scope for further model improvement.
* CPU inference performance depends on the available system resources.
* The application has been tested in a local Docker environment; public production deployment was not demonstrated.
* Production deployment would require additional security, monitoring, resource management, and performance testing.

### Final Testing Status

**Core Application Functionality:** Successfully Demonstrated

**Docker Containerization:** Successfully Demonstrated

**Model and API Integration:** Successfully Demonstrated

**Streamlit Integration:** Successfully Demonstrated

**Container Restart and Network Verification:** Successfully Demonstrated

**Testing Documentation:** Complete

**Overall Result:** The core application requirements were demonstrated successfully, with supporting evidence documented for all twelve test cases.
