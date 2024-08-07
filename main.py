import streamlit as st

# Set the title and logo
st.set_page_config(page_title="Ethical Hacking Exam Prep", page_icon="🔒")

# Logo and Title
st.image("https://wallpapers.com/images/hd/xxxtentacion-blue-hair-in-dark-room-o6z10kxfk1w3se67.jpg", width=100)  # Replace with your own logo URL
st.title("Ethical Hacking Exam Preparation")

# Description
st.write("Welcome to our Ethical Hacking exam preparation platform. Choose the right option for your needs:")

# Dropdown for selecting an exam
exam = st.selectbox("Select an exam:", ["EHE", "eJPT", "CEH", "OSCP", "Other"])  # Add other exams as needed

# Pricing and options based on selected exam
if exam == "EHE":
    st.subheader("Exam: EHE (Ethical Hacking Essentials)")
    st.write("**Write the Exam without Explanation**")
    st.write("Price: ₹1200/-")
    st.write("Take the exam without any explanations or hints.")

    st.write("**Write the Exam with Explanation**")
    st.write("Price: ₹1500/-")
    st.write("Get detailed explanations for each question after you complete the exam.")

    st.write("**Help During the Exam**")
    st.write("Price: ₹1700/-")
    st.write("Receive guidance and assistance during the exam.")

elif exam == "eJPT":
    st.subheader("Exam: eJPT (eLearnSecurity Junior Penetration Tester)")
    st.write("**Write the Exam without Explanation**")
    st.write("Price: ₹1400/-")
    st.write("Take the exam without any explanations or hints.")

    st.write("**Write the Exam with Explanation**")
    st.write("Price: ₹1600/-")
    st.write("Get detailed explanations for each question after you complete the exam.")

    st.write("**Help During the Exam**")
    st.write("Price: ₹1800/-")
    st.write("Receive guidance and assistance during the exam.")

elif exam == "CEH":
    st.subheader("Exam: CEH (Certified Ethical Hacker)")
    st.write("**Write the Exam without Explanation**")
    st.write("Price: ₹1300/-")
    st.write("Take the exam without any explanations or hints.")

    st.write("**Write the Exam with Explanation**")
    st.write("Price: ₹1500/-")
    st.write("Get detailed explanations for each question after you complete the exam.")

    st.write("**Help During the Exam**")
    st.write("Price: ₹1700/-")
    st.write("Receive guidance and assistance during the exam.")

elif exam == "OSCP":
    st.subheader("Exam: OSCP (Offensive Security Certified Professional)")
    st.write("**Write the Exam without Explanation**")
    st.write("Price: ₹2000/-")
    st.write("Take the exam without any explanations or hints.")

    st.write("**Write the Exam with Explanation**")
    st.write("Price: ₹2500/-")
    st.write("Get detailed explanations for each question after you complete the exam.")

    st.write("**Help During the Exam**")
    st.write("Price: ₹3000/-")
    st.write("Receive guidance and assistance during the exam.")

else:
    st.subheader("Other Exams")
    st.write("**Write the Exam without Explanation**")
    st.write("Price: ₹1200/-")
    st.write("Take the exam without any explanations or hints.")

    st.write("**Write the Exam with Explanation**")
    st.write("Price: ₹1500/-")
    st.write("Get detailed explanations for each question after you complete the exam.")

    st.write("**Help During the Exam**")
    st.write("Price: ₹1700/-")
    st.write("Receive guidance and assistance during the exam.")

# Additional Services
st.header("Additional Services")

st.write("**Hint for a Question**")
st.write("Price: ₹200/-")
st.write("Receive a hint for a specific question during the exam.")

st.write("**Help in the Middle of the Exam**")
st.write("Price: ₹400/-")
st.write("Get assistance in the middle of the exam.")

# Contact Information
st.header("Contact Us")
st.write("For more information or to get in touch, please contact us on [Telegram](https://t.me/YourTelegramUsername).")  # Replace with your Telegram username

# Disclaimer
st.write("---")
st.write("**Disclaimer:** This is a mock-up site for demonstration purposes. Actual pricing and services may vary.")
