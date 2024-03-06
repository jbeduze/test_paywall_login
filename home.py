import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import html
from streamlit.components.v1 import components


st.title ("login and stripe payment (test mode)")
st.write("multi-step layout")



container1 = st.container(border=True)
col1, col2 = st.columns(2)
with container1:
    st.write("Daddy Bets: Terms and conditions")
    if st.button("Accept Terms and conditions", use_container_width=True):
        with col1:
            stripe_js = """
            <script async src="https://js.stripe.com/v3/buy-button.js"></script>
            <stripe-buy-button
            buy-button-id="buy_btn_1OrDTGDvYq7iSz1pnNP8cS17"
            publishable-key="pk_live_51OEP9VDvYq7iSz1pjs0Tqqar3fcDpYlKos337xuQGcL54KdZYiMDdi2eitpFPMzAMKXczUpODNmavddLAaJNSKpE006EvUkYSU"
            ></stripe-buy-button>
            """
            html(stripe_js, height=250)
        with col2:
            st.write("placeholder for Stripe QR code")


        

        