import streamlit as st
import subprocess
import time
import datetime
import pandas as pd
#import pybase64 as base64

import streamlit as st





def get_final_text():
  """Returns the final text from the keyboard.py file."""

  # Start the keyboard.py file in a separate process.
  process = subprocess.Popen(["python", "keyboard.py"], stdout=subprocess.PIPE)

  # Read the output of the process.
  final_text = process.communicate()[0]

  # Decode the output to a string.
  final_text = final_text.decode("utf-8")

  # Close the process.
  process.terminate()

  return final_text


text_history={}
def start_open_cvcode():
    date=datetime.datetime.now()
    text_history[date]=get_final_text()

    st.write(text_history[date])

    with open("output.csv", "a") as f:
  # Write the output to the file
        point=str(date)+" "+str(text_history[date])
        f.write(point) 
        f.close()
        


def history(text_history):
    df=pd.read_csv("output.csv",header=0,sep=" ")
    
    st.dataframe(df)

def main():
    st.set_page_config(page_title="Virtual keyboard",page_icon=":keyboard:",layout="centered" )
  
   

# Set the background color to black
    #st.set_page_config(layout="wide", page_title="My Streamlit App", page_icon=":robot:", initial_sidebar_state="collapsed", menu_items=None, background_color="#000000")


    st.title("Virtual Keyboard")


    if st.button("Start Camera"):
        start_open_cvcode()

    if st.button("History"):
        history(text_history)



if __name__=="__main__":
    main()






