import mysql.connector
import streamlit as st
conn = mysql.connector.connect(
    host = st.secrets["host"],
    user = st.secrets["user"],
    port = st.secrets["port"],
    password = st.secrets["password"],
    database = st.secrets["database"]
)
cursor = conn.cursor()

cursor.execute(""" 
               create table if not exists users (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) ,
                   email VARCHAR(255) UNIQUE,
                   password VARCHAR(255)
               )
               """)

cursor.execute("""
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

conn.commit()
print("Tables created successfully")