import pickle
import sklearn
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header

#Reading the data
data = pd.read_csv("final1.csv")
# Streamlit page custom design
class App:
    def model(self):
        # Setting Page Configuration
        st.set_page_config(page_title="Flat resale prediction | By Viswanathan", layout="wide")
        # Creating the option menu in the sidebar
        with st.sidebar:
            selected = option_menu(
                menu_title="FRP",
                options=["Flat resale_Prediction",],
                icons=['graph-up-arrow', ''],
                menu_icon='alexa',
                default_index=0
            )

        if selected == "Flat resale_Prediction":
            col1, col2, col3 = st.columns([4, 10, 2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 80px;'><span style='color: cyan;'>Flat resale price</span><span style='color: white;'> Prediction</span> </h1>",
                    unsafe_allow_html=True)
            col1, col2, col3 = st.columns([4, 10, 5])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            col1, col2, col3 = st.columns([2, 10, 2])
            # Start from options
            col2.write("")
            with col2:
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 30px;'><span style='color: cyan;'>selling_month </h1>", unsafe_allow_html=True)
                selling_month = st.selectbox(' ', [1,2,3,4,5,6,7,8,9,10,11,12])

                # ________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>selling_year </h1>", unsafe_allow_html=True)
                selling_year = st.selectbox('    ',[1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
                                            2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                                            2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022,
                                            2023, 2024])
                # ________________________________________________________________________

                st.write("")
                st.write("")

                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Town </h1>", unsafe_allow_html=True)
                town_dict = dict(zip(data['town'].unique(), data['town_code'].unique()))
                town_list = data['town'].unique()
                town_key = st.selectbox('Town', options=town_list)
                town = town_dict[town_key]
                st.write("")

                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Store_min </h1>", unsafe_allow_html=True)
                storey_min = st.number_input('', min_value=1, max_value=49, value=10,)

                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Store_max </h1>",
                            unsafe_allow_html=True)
                storey_max = st.number_input('', min_value=3, max_value=51, value=12,)
                st.write("")

                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Floor_area_sqft </h1>", unsafe_allow_html=True)
                floor_area_sqm = st.number_input('', min_value=28.0, max_value=307.0, value=31.0	,)

                st.write("")
                st.write("")

                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Flat_Model </h1>", unsafe_allow_html=True)
                model_dict = dict(zip(data['flat_model'].unique(), data['flat_modelcode'].unique()))
                model_list = data['flat_model'].unique()
                flat_model = st.selectbox('Flat Model', options=model_list)
                flat_modelcode = model_dict[flat_model]


                st.write("")

                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>lease_commence_date</h1>", unsafe_allow_html=True)
                lease_commence_date = st.selectbox('  ', [1977, 1976, 1978, 1979, 1984, 1980, 1985, 1981, 1982, 1986, 1972,
                                                          1983, 1973, 1969, 1975, 1971, 1974, 1967, 1970, 1968, 1988, 1987,
                                                          1989, 1990, 1992, 1993, 1994, 1991, 1995, 1996, 1997, 1998, 1999,
                                                          2000, 2001, 1966, 2002, 2006, 2003, 2005, 2004, 2008, 2007, 2009,
                                                          2010, 2012, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2022,
                                                          2020])

                st.write("")
                st.write("")


                predict_data = [selling_month, selling_year, town, storey_min, storey_max,
                                floor_area_sqm,flat_modelcode,lease_commence_date]

                with open('SF_regression.pkl', 'rb') as f:
                    model = pickle.load(f)
            col1, col2, col3 = st.columns([10, 1, 10])

            with col1:
                st.write("")
                if st.button('Process'):
                    x = model.predict([predict_data])
                    st.markdown(
                        f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Predicted Flat Resale: </span><span style='color: white;'> {x[0]}</span> </h1>",
                        unsafe_allow_html=True)


# Object
Object = App()
Object.model()