import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import html
from streamlit.components.v1 import components
from streamlit_extras.add_vertical_space import add_vertical_space


# Initialize session state variables if they don't exist
if 'terms_accepted' not in st.session_state:
    st.session_state['terms_accepted'] = False
if 'customer_status' not in st.session_state:
    st.session_state['customer_status'] = None  # 'new' or 'returning'

cntner1 = st.container(border=True)

with cntner1:
    with st.expander(
        "Daddy Bets: Terms and conditions",
        expanded=True
        ):
    
        # Accepting terms and conditions
        if st.button("Accept Terms and conditions", use_container_width=True) or st.session_state['terms_accepted']:
            st.session_state['terms_accepted'] = True  # Terms accepted
        if st.session_state['terms_accepted']:
            st.success('You have accepted the terms and conditions, thank you')
            cols = st.columns(2)
            # Asking if the customer is new or returning
            if st.session_state['customer_status'] is None:
                if cols[0].button("Returning Customer"):
                    st.session_state['customer_status'] = 'returning'
                elif cols[1].button("New Customer"):
                    st.session_state['customer_status'] = 'new'

            # Handling returning customer
            if 'customer_status' in st.session_state and st.session_state['customer_status'] == 'returning':
                # Placeholder for the form
                placeholder = st.empty()
                
                # Preset login credentials
                actual_email = "email@example.com"
                actual_password = "password123"
                
                # Insert a form in the container
                with placeholder.form("login"):
                    st.markdown("#### Enter your credentials")
                    email = st.text_input("Email")
                    password = st.text_input("Password", type="password")
                    submit = st.form_submit_button("Login")
                
                # Check if the form was submitted and the credentials match
                if submit:
                    if email == actual_email and password == actual_password:
                        # Clear the form/container and display a success message
                        placeholder.empty()
                        st.success("Login successful")
                    else:
                        # Display an error message if login fails
                        st.error("Login failed")
                    
            # Handling new customer
            elif st.session_state['customer_status'] == 'new':
                        col = st.columns(2)
                        with col[0]:
                            stripe_js = """
                            <script async src="https://js.stripe.com/v3/buy-button.js"></script>
                            <stripe-buy-button
                            buy-button-id="buy_btn_1OrDTGDvYq7iSz1pnNP8cS17"
                            publishable-key="pk_live_51OEP9VDvYq7iSz1pjs0Tqqar3fcDpYlKos337xuQGcL54KdZYiMDdi2eitpFPMzAMKXczUpODNmavddLAaJNSKpE006EvUkYSU"
                            ></stripe-buy-button>
                            """
                            html(stripe_js, height=250)
                        with col[1]:
                            st.image('qr_14kcPxclKdlic2k6oq.png', width= 210) 
