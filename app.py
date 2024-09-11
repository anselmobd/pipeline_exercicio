import streamlit as st


def main():
    st.title("Sistema CRM")
    email = st.text_input("e-mail")
    data = st.date_input("data")
    hora = st.time_input("hora")
    valor = st.number_input("valor unitário", min_value=0.0, format="%.2f")
    quant = st.number_input("quantidade", min_value=1, step=1)
    produto = st.selectbox("produto", ["Gemine", "ChatGPT", "Llama"])

    if st.button("Salvar"):
        st.write("email", email)
        st.write("data", data)
        st.write("hora", hora)
        st.write("valor", valor)
        st.write("quant", quant)
        st.write("produto", produto)


if __name__ == '__main__':
    main()
