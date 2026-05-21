import streamlit as st
from db_c import conn_obj, cursor_obj  
import cloudinary
import cloudinary.uploader 
st.title("Media Platform")


cloudinary.config(
    cloud_name=st.secrets["cloud_name"],
    api_key=st.secrets["api_key"],
    api_secret=st.secrets["api_secret"]
)


if "user" not in st.session_state:
    st.session_state.user = None

def dashboard():
    st.sidebar.success("welcome user")
    opt=st.sidebar.selectbox("choose :-- ",["uploadFiles","viewFiles","Logout"])
    st.header("dashboard")  

    if opt == "uploadFiles":
        st.header("upload yr files here")
        choosedFile=st.file_uploader("choose file",type=["pdf","jpg","jpeg","png","mp3","mp4"]) 

        if choosedFile is not None:
            st.write(choosedFile.name)
            st.write(choosedFile.type)

            if "image" in choosedFile.type:
               st.image(choosedFile)
            elif "video" in choosedFile.type:
               st.video(choosedFile)
            elif "audio" in choosedFile.type:
               st.audio(choosedFile)  

            if st.button("upload file to cloudinary"):
                uploaded_dict_obj=cloudinary.uploader.upload(choosedFile,resource_type="auto") 
                url=uploaded_dict_obj["secure_url"]             
                st.write(url)
                st.write("file uploaded to cloudinary")
    elif opt == "Logout":
        st.session_state.user=None
        st.success("logout successfully...")
        st.rerun()


def login():
    st.header("login")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        button = st.form_submit_button("Login")

        if button:
            query = "select*from users where email = %s and password = %s"
            values = (email,password)
            cursor_obj.execute(query,values)
            logged_in_user = cursor_obj.fetchone()

            st.session_state.user = logged_in_user
            st.write("Logged in successfully")
            st.rerun()


def signup():
    st.header("Signup")
    with st.form("signup_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password",type = "password")
        button = st.form_submit_button("Signup")


        if button:
            try:
                query="insert into users(name,email,password) values(%s,%s,%s)"
                values=(name,email,password)
                cursor_obj.execute(query,values)
                conn_obj.commit()
                st.write("user added successfully ")
            except Exception as e:
                st.error(e)

if st.session_state.user == None:
    login_tab,signup_tab = st.tabs(
    ["Login","SignUp"]
    )
    with signup_tab:
        signup()

    with login_tab:
        login()    
else:
    dashboard()
