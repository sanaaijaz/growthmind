import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")

st.title("Growth Mindset AI Project Web App With Streamlit")

st.header("🌠Welcome To My Growth Journey!")
st.write('"A growth mindset helps us embrace challenges, learn from mistakes, and keep improving every day."')

# Quote section
st.header("Today's Growth Mindset Quote")
st.write('"Success comes from learning, not from giving up. Every challenge is a chance to grow."')
st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challange you are facing:")

#condition
if user_input:
    st.success(f"your facing: {user_input}. keep pushing forwad towards your goal✨")
else:
    st.warning("Tell us about Your challenge to get starter!")

    #reflexing
    st.header("Reflect Your Learning")
    reflection = st.text_area("Write Your Outcome here")

    if reflection:
        st.success(f" Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you to grow! share your difficulties")

        #achivements
        st.header("Celebrate Your Wins!")
        achievements =st.text_input("Share something you've recently accomplished:")
        if achievements:
            st.success(f"·̩̩̥͙＊*•̩̩͙✩•̩̩͙*˚ Amazing! You achived: {achievements}")
        else:
            st.info("Big or small , every acheivement counts! Share one now😊")   
            

            #footer
            st.write("---")
            st.write("🚀 Keep going—every small step brings you closer to your goal! ⭐")
            st.write("*⛔ Created By Sana Aijaz* ")

