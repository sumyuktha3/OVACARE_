import streamlit as st
from home_page_content import show_home_page_content
from prediction_page import pcos_prediction_app
from pcos_details_content import show_pcos_details_content
from no_pcos_details_content import show_no_pcos_details_content


# Define the Streamlit app
def main():
    st.sidebar.title('Navigation')

    # Sidebar navigation
    page = st.sidebar.selectbox("Go to", ["OVACARE", "PREDICTION", "POSITIVE", "NEGATIVE"])

    if page == "OVACARE":
        image_path = "C:\\userspace\\daya\\python\\samu_proj\\web_page\\logo.jpeg"  
        circle_style = """
        <style>
        img {
            border-radius: 10%;
        }
        </style>
        """

        # Display circular image using st.markdown() with the defined CSS
        st.markdown(circle_style, unsafe_allow_html=True)
        st.image(image_path, use_column_width=True)
        st.markdown(show_home_page_content(), unsafe_allow_html=True)
    
    elif page == "PREDICTION":
        prediction_result = pcos_prediction_app()
        if prediction_result is not None:
            st.write(f"Prediction: {prediction_result}")
        st.markdown("<p style='font-family: Mansalva, serif; color: #FF0100; font-size:30px;'> FUTURE-PROOF YOUR PCOS </p>", unsafe_allow_html=True)

    elif page == "POSITIVE":
        st.markdown(show_pcos_details_content(), unsafe_allow_html=True)

    elif page == "NEGATIVE":
        st.markdown(show_no_pcos_details_content(), unsafe_allow_html=True)

if __name__ == '__main__':
    main()

