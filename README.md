# **CardioCare ❤️ AI-Powered Website**

## **⚠️ Important Warning**
This project **focuses on integrating AI into the web** to provide an initial overview of **heart disease risks**.  

**The AI predictions provided are not for medical reference!**
- **CardioCare is not a medical diagnostic tool.**
- **The predictions shown are based solely on the AI model and the data entered by the user.**
- **Please consult your doctor or a healthcare professional for accurate diagnosis and treatment.**
---

## **Project Goals 🎯**
To provide health education and an initial overview of heart disease risks by integrating AI technology into an easy-to-use web platform.

## **About the Project 📋**
**CardioCare** is an interactive landing page that helps users:
- **Learn about heart disease education** through informative content.
- **Check their heart health risk** using **AI** trained with **Scikit-Learn**.

This project combines **AI technology** and **modern web** to create an interactive and user-friendly experience.

---

## **Key Features ✨**
1. **Heart Disease Education**  
   Complete and easy-to-understand information about heart disease risks.
2. **Heart Disease Risk Check**  
   - Users fill out a simple form (age, blood pressure, cholesterol, etc.).
   - The Flask backend runs the AI model to predict the health risk.
   - The result, showing the **initial risk**, is displayed on the ReactJS frontend.

---

## **Technologies Used 🛠️**
### **Frontend**
1. ReactJS: Building the interactive user interface.
2. Axios: Connecting the React frontend with the Flask backend.
3. TailwindCSS: Modern and responsive styling.
4. Framer Motion: Make any design animated.
### **Backend**
1. Flask: To create the API that receives data from the user and processes the AI model.
2. Scikit-Learn: Training and running the heart disease risk prediction model.
3. Pickle: Storing the trained AI model for future use.

---

# API Documentation 📄
## Endpoint: `/predict`
**Method:** `POST`  
**Description:**  
This endpoint is used to send user data and receive a prediction regarding the heart disease risk based on the provided input.

---

### Required Data (Request Body)
The following data must be sent in JSON format:

| **Parameter**   | **Data Type** | **Description**                                           |
|-----------------|---------------|---------------------------------------------------------|
| `age`           | `float`       | User's age (e.g., `45.0`)                                 |
| `sex`           | `int`         | Gender (1 = Male, 0 = Female)                            |
| `cp`            | `int`         | Chest pain type (using category numbers)                 |
| `trestbps`      | `float`       | Resting blood pressure (e.g., `130.0`)                   |
| `chol`          | `float`       | Cholesterol level (e.g., `250.0`)                        |
| `fbs`           | `int`         | Fasting blood sugar (1 = >120 mg/dL, 0 = ≤120 mg/dL)     |
| `restecg`       | `int`         | Resting electrocardiographic results (category number)   |
| `thalach`       | `float`       | Maximum heart rate during physical activity              |
| `exang`         | `int`         | Exercise-induced chest pain (1 = Yes, 0 = No)            |
| `oldpeak`       | `float`       | ST depression during exercise test (e.g., `1.2`)        |
| `slope`         | `int`         | Slope of the peak exercise ST segment (category number) |
| `ca`            | `int`         | Number of major vessels colored by fluoroscopy           |
| `thal`          | `int`         | History of thalassemia (category number)                |

Once the data is submitted, the server will return a response in JSON format containing the prediction result and suggestions for further steps.

#### Response Structure:
```json
{
  "prediction": "Heart Disease Detected",
  "suggestion": "We recommend consulting a doctor for further evaluation."
}
