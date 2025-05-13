import streamlit as st
from reto_medicom_eda import *


def main():   
    # Title of the app
    st.title("PredApp")

    ID = int(st.text_input("ID:", ""))
    if (ID not in IDs) or type(ID) != int: 
        st.error("Please Select a valid ID.")
    else:

        Type = st.selectbox("Type: ", ['Client', 'Product'])
 
        if Type == 'Client':
            Type = 'cli' 
        else:  
            Type = 'mat'

        # Main section
        if st.button("Submit") and ID and Type:

            # Step 4: Print the Description
            st.subheader("Current State:")
            description, recommendation, valor_cliente = information(ID, Type, 43)  # Assuming Description takes ID and Type as arguments
            st.write(description)

            
            st.subheader("Prob of Buying")
            
            st.pyplot(prob_plot(ID, Type))  # This ensures the plot is displayed in Streamlit

            
            st.subheader("Estimated Sales:")
            # Assuming Forecast generates a plot directly
            st.pyplot(predict_sales(Type, ID))  # This ensures the plot is displayed in Streamlit
            
            if Type == 'cli':
                st.subheader('Client Value')
                 
                st.write(valor_cliente)
                st.subheader('Prods: ')
                st.write(f'Total bought products: {prod_bought(ID)}')
                #st.pyplot(top_prod(ID))
            else: 
                st.subheader('Clients: ')
                st.write(f'Total clients: {buyers(ID)}')
                #st.pyplot(top_buyers(ID))
            
            
            st.subheader("Recomendation")
            
            st.write(recommendation)

            return 0
main()