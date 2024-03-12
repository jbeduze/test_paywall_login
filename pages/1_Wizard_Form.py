import streamlit as st
from config import Terms_conditions as TC
from st_paywall import add_auth

if 'terms_accepted' not in st.session_state:
    st.session_state['terms_accepted'] = False
if 'customer_status' not in st.session_state:
    st.session_state['customer_status'] = None  # 'new' or 'returning'

with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


if 'current_step' not in st.session_state:
    st.session_state['current_step'] = 1

if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'Grid'

### maintains the user's location within the wizard
def set_form_step(action,step=None):
    if action == 'Next':
        st.session_state['current_step'] = st.session_state['current_step'] + 1
    if action == 'Back':
        st.session_state['current_step'] = st.session_state['current_step'] - 1
    if action == 'Jump':
        st.session_state['current_step'] = step

### used to toggle back and forth between Grid View and Form View
def set_page_view(target_view):
    st.session_state['current_view'] = target_view


def render_wizard_view(): 
    with st.expander('',expanded=True):     
        sf_header_cols = st.columns([1, 1.75, 1])
        
        with sf_header_cols[1]:            
            st.subheader("Welcome to Daddy Bets, Let's get you logged in")
    
    # determines button color which should be red when user is on that given step
    TC_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
    users_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
    pymnt_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
    runDB_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

    step_cols = st.columns([.5, .85, .85, .85, .85, .5])    
    step_cols[1].button('Terms and conditions', on_click=set_form_step, args=['Jump', 1], type=TC_type)
    step_cols[2].button('New/Old Users', on_click=set_form_step, args=['Jump', 2], type=users_type)        
    step_cols[3].button('Payment Section', on_click=set_form_step, args=['Jump', 3], type=pymnt_type)      
    step_cols[4].button('Run Daddy Bets', on_click=set_form_step, args=['Jump', 4], type=runDB_type)

                     
       
    ('---')
    if st.session_state['current_step'] == 1:
        cntner1 = st.container(border=True)

        with cntner1:
            with st.expander("Daddy Bets: Terms and conditions", expanded=True):
                st.write("ooooh, look what you made me do")
        if st.button("Accept Terms and conditions", use_container_width=True) or st.session_state['terms_accepted']:
            st.session_state['terms_accepted'] = True  # Terms accepted
        if st.session_state['terms_accepted']:
            st.success('You have accepted the terms and conditions, on step closer to sitting at the big table')

    elif st.session_state['current_step'] == 2:
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

            if 'customer_status' in st.session_state and st.session_state['customer_status'] =='new':
                col = st.columns(2)
                with col[0]:
                    st.write("Pay up, click the link to the right")
                with col[1]:
                    add_auth(required= True, login_button_text="Proceed to payment", login_button_color="006667", login_sidebar= False, )

    elif st.session_state['current_step'] == 3:
        st.write("monkey buts")
    elif st.session_state['current_step'] == 4:
        st.write("completed the following: 1. agreed to terms and conditions, 2. logged in or signed up, 3. been a boss the whole time. here are your credentials (  )")
        st.button("prepare for winning", use_container_width= True)
    ('---')
    disable_back_button = True if st.session_state['current_step'] == 1 else False
    disable_next_button = True if st.session_state['current_step'] == 4 else False

    form_footer_cols = st.columns([5,1,1,1.75])

    form_footer_cols[0].button('Cancel', on_click=set_page_view, args=['Grid'])
    form_footer_cols[1].button('Back', on_click=set_form_step, args=['Back'], disabled=disable_back_button)
    form_footer_cols[2].button('Next', on_click=set_form_step, args=['Next'], disabled=disable_next_button)
    form_footer_cols[3].button('Rerun web app', disabled=True)


if st.session_state['current_view'] == 'Grid':
    render_wizard_view()