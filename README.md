# Singapore-Resale-Flat-Prices-Prediction
## Intro
The project aims to create a user-friendly web application using machine learning. It predicts resale prices of flats in Singapore based on historical data, aiding potential buyers and sellers in estimating a flat's resale value

## Key Technologies and Skills

- Python
- Pandas
* Scikit-Learn
- Matplotlib
* Seaborn
- Pickle
* Streamlit
  
**Data Collection**: Obtain the dataset from.[Data Source](https://beta.data.gov.sg/collections/189/view)

**Data Understanding:** Before diving into modeling, it's crucial to gain a deep understanding of your dataset. Start by identifying the types of variables within it, distinguishing between continuous and categorical variables, and examining their distributions.

**Data Preprocessing**: clean the data, handle missing values, and perform feature engineering.

## Regression Algorithm

**Algorithm Assessment:** In the realm of regression, our primary objective is to predict the continuous variable of Flat resale price. Our journey begins by splitting the dataset into training and testing subsets. We systematically apply various algorithms, evaluating them based on training and testing accuracy using the R2 (R-squared) metric, which signifies the coefficient of determination. This process allows us to identify the most suitable base algorithm tailored to our specific data.

**Algorithm Selection:** After a thorough evaluation, Random Forest Regressor, emerges with commendable testing accuracy. However, it strikes a balance between interpretability and accuracy, making it a fitting choice of Flat resale price.

**Model Persistence:** We conclude this phase by saving our well-trained model to a pickle file. This strategic move enables us to effortlessly load the model whenever needed, streamlining the process of making predictions on selling prices in future applications.

# Overview UI Dashboard
![sam 1](https://github.com/Viswanathan25/Singapore-Resale-Flat-Prices-Prediction/assets/131848906/c3a763d2-ee47-44c5-81f2-87c6a9e0eed9)
![sam2](https://github.com/Viswanathan25/Singapore-Resale-Flat-Prices-Prediction/assets/131848906/0fe0c1e1-eaa7-4add-9c3b-c9b0de2c03c5)
![sam3](https://github.com/Viswanathan25/Singapore-Resale-Flat-Prices-Prediction/assets/131848906/3641adfd-5407-4cee-a4a9-2b07ac051788)
![sam4](https://github.com/Viswanathan25/Singapore-Resale-Flat-Prices-Prediction/assets/131848906/d6dbb7ea-84c1-4daf-96c1-b67b4a39448d)

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

## connect 
[Linkedin](https://www.linkedin.com/in/viswanathan-sankaran-vis25)
