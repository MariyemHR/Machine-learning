import streamlit as st
import pickle

with open('kmeans_model7.pkl', 'rb') as file:
    model = pickle.load(file, encoding='latin1')

def main():
    st.title('Custmers group')
    amount = st.number_input('Enter amount', min_value=0.0, value=0.0)
    frequency = st.number_input('Enter frequency', min_value=0, value=0)
    recency = st.number_input('Enter recency', min_value=0, value=0)

    if st.button('Predict'):
        int_features = [amount, frequency, recency]
        prediction = model.predict([int_features])
        output = prediction[0]

        if output == 0:
            res = "Plat"
        elif output == 2:
            res = "Gold"
        else:
            res = "Basic"

        st.write('You are in the following group: {}'.format(res))

if __name__ == '__main__':
    main()
