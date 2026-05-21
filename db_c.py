import mysql.connector
import streamlit as st
conn_obj= mysql.connector.connect(
    host = st.secrets["host"],
    user = st.secrets["user"],
    port = st.secrets["port"],
    password = st.secrets["password"],
    database = st.secrets["database"]
)
cursor_obj = conn_obj.cursor()

cursor_obj.execute(""" 
               create table if not exists users (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) ,
                   email VARCHAR(255) UNIQUE,
                   password VARCHAR(255)
               )
               """)

cursor_obj.execute("""
                 create table if not exists files (
                      id int auto_increment primary key,
                      user_id int,
                      filename varchar(255),
                      file_type varchar(255),
                       file_url text,
                        uploaded_at timestamp default current_timestamp,
                      foreign key (user_id) references users(id)
                 )
                 """)

conn_obj.commit()
print("Tables created successfully")