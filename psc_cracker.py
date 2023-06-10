import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import json
import random
# Create the quiz form


score = 0
maths_score=0
correct_answers=[]
maths_correct_answers=[]
wrong_answers=[]
maths_wrong_answers=[]
tab1,tab2,tab3,tab4,tab5=st.tabs(["Home","maths","science","general knowledge","Add your questions here"])
def load_quiz_data(file_path):
    with open(file_path, 'r') as file:
        quiz_data = json.load(file)
    return quiz_data

def display_question(question):
    st.write(question['question'])
    options = question['options']
    for i, option in enumerate(options):
        st.write(f"{chr(ord('A') + i)}) {option}")

def main():
    st.title("Quiz Program")
    


with tab4:
    st.title("Sample General knowledge questions")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("General Knowledge.png")
    gk_quiz_data = load_quiz_data('quiz_questions gk.json')
 
  
    for i, question in enumerate(gk_quiz_data):
        st.info(f"{i+1}. {question['question']}")
        user_answer = st.selectbox("Select your answer:", question['choices'])
        if user_answer == question['correct_answer']:
            score += 1
            correct_answers.append(f"question {i+1}")
        elif user_answer==question["choices"][0]:
            pass  
        else:
            wrong_answers.append(f"question {i+1}")  

    # Display the score
    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("4.jpg",width=100)
    if st.button("check your marks"):
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.info(f"You scored {score} out of {len(gk_quiz_data)}")
        labels = ['Correct Answers', 'Wrong Answers']
        values = [len(correct_answers),len(wrong_answers)]
        colors=["green","red"]

        # Create a bar chart
        fig, ax = plt.subplots()
        ax.bar(labels, values,color=colors)

        # Set chart title and labels
        ax.set_title('Correct vs Wrong Answers')
        ax.set_xlabel('Answer Type')
        ax.set_ylabel('Count')

        # Display the chart in treamlit
        st.pyplot(fig)


        if 0<=score<=5:
            st.warning("work hard...")
        elif 6<=score<=8:
            st.snow()
            st.info("good work...keep trying yu can improve") 
        else:
            st.snow()
            st.success("excellent...")       
    # Add a reset button
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Reset"):
        score = 0
    col1,col2=st.columns(2)
    with col1: 
        st.markdown("<hr>", unsafe_allow_html=True)   
        if st.button("correct answers"):
            for i in correct_answers:
                st.success(i) 
    with col2: 
        st.markdown("<hr>", unsafe_allow_html=True)             
        if st.button("wrong answer"):
            for i in wrong_answers:
                st.error(i)         
with tab1:
    st.title("PSC CRACKER")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Boost your knowledge.")
    st.image("1.jpg")
    
    st.subheader("""Dear users,

A warm welcome to our PSC CRACKER Quiz Application! We are excited to bring you this platform where you can test your knowledge and prepare for the upcoming Kerala Public Service Commission (PSC) exams.

Our quiz application is designed to help you become familiar with the format and types of questions that appear in the Kerala PSC exams. With a vast database of questions covering a range of subjects and topics, you can challenge yourself and learn something new every day.

Whether you are a first-time user or a regular quizzer, our user-friendly interface and intuitive features will make your experience seamless and enjoyable. With the ability to track your progress and compare scores with others, you can track your growth and measure your success.

We are committed to providing you with the best learning experience possible, and we hope that you find our PSC CRACKER Quiz Application helpful in your exam preparation. Thank you for choosing us and we wish you the best of luck in your endeavors!

Sincerely,
The PSC CRACKER Quiz Application Team""")
with tab2:
    st.title("Maths model questions")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("2.jpg",width=700)
    st.markdown("<hr>", unsafe_allow_html=True) 
    st.header("Answer the following questions.")
    maths_quiz_data = load_quiz_data('quiz_maths.json')
    

    
    for i, question in enumerate(maths_quiz_data):
        st.info(f"{i+1}. {question['question']}")
        user_answer = st.selectbox("Select your answer:", question['choices'])
        if user_answer == question['correct_answer']:
            maths_score += 1
            maths_correct_answers.append(f"question {i+1}")
        elif user_answer==question["choices"][0]:
            pass  
        else:
            maths_wrong_answers.append(f"question {i+1}")  

    # Display the score
    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("4.jpg",width=100)
    if st.button("check your marks",key="key"):
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.info(f"You scored {maths_score} out of {len(maths_quiz_data)}")
        labels = ['Correct Answers', 'Wrong Answers']
        values = [len(maths_correct_answers),len(maths_wrong_answers)]
        colors=["green","red"]

        # Create a bar chart
        fig, ax = plt.subplots()
        ax.bar(labels, values,color=colors)

        # Set chart title and labels
        ax.set_title('Correct vs Wrong Answers')
        ax.set_xlabel('Answer Type')
        ax.set_ylabel('Count')

        # Display the chart in treamlit
        st.pyplot(fig)


        if 0<=maths_score<=5:
            st.warning("work hard...")
        elif 6<=maths_score<=8:
            st.snow()
            st.info("good work...keep trying yu can improve") 
        else:
            st.snow()
            st.success("excellent...")       

    # Add a reset button
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Reset",key="key1"):
        maths_score = 0
    col1,col2=st.columns(2)
    with col1:  
        st.markdown("<hr>", unsafe_allow_html=True)  
        if st.button("correct answers",key="key2"):
            for i in maths_correct_answers:
                st.success(i) 
    with col2:  
        st.markdown("<hr>", unsafe_allow_html=True)            
        if st.button("wrong answer",key="key3"):
            for i in maths_wrong_answers:
                st.error(i)     
with tab3:  
    st.title("Science sample questions") 
    st.markdown("<hr>", unsafe_allow_html=True)
    st.image("3.webp")
    st.markdown("<hr>", unsafe_allow_html=True)
    science_quiz_data = load_quiz_data('quiz_science.json')
    
    science_correct_answers=[]
    science_wrong_answers=[]
    science_score=0
    
    
    

    
    
   
    
    
    for i, question in enumerate(science_quiz_data):
        st.info(f"{i+1}. {question['question']}")
        user_answer = st.selectbox("Select your answer:", question['choices'],key=i)
        if user_answer == question['correct_answer']:
            science_score += 1
            science_correct_answers.append(f"question {i+1}")
        elif user_answer==question["choices"][0]:
            pass  
        else:
            science_wrong_answers.append(f"question {i+1}")  

    # Display the score
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Check your marks hear")
    st.image("4.jpg",width=100)
    if st.button("check your marks",key="key4"):
        
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.info(f"You scored {science_score} out of {len(science_quiz_data)}")
        labels = ['Correct Answers', 'Wrong Answers']
        values = [len(science_correct_answers),len(science_wrong_answers)]
        colors=["green","red"]

        # Create a bar chart
        fig, ax = plt.subplots()
        ax.bar(labels, values,color=colors)

        # Set chart title and labels
        ax.set_title('Correct vs Wrong Answers')
        ax.set_xlabel('Answer Type')
        ax.set_ylabel('Count')

        # Display the chart in treamlit
        st.pyplot(fig)


        if 0<=science_score<=5:
            st.warning("work hard...")
        elif 6<=science_score<=8:
            st.snow()
            st.info("good work...keep trying yu can improve") 
        else:
            st.snow()
            st.success("excellent...")  

    # Add a reset button
    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("Reset",key="key5"):
        science_score = 0
    col1,col2=st.columns(2)
    with col1: 
        st.markdown("<hr>", unsafe_allow_html=True) 
        if st.button("correct answers",key="key6"):
            for i in science_correct_answers:
                st.success(i) 
    with col2:
        st.markdown("<hr>", unsafe_allow_html=True)              
        if st.button("wrong answer",key="key7"):
            for i in science_wrong_answers:
                st.error(i)    
with tab5:
    st.title("Upload your questions hear.")
    st.image("question-mark-2492009_1280-1080x598.webp")
    tab1,tab2,tab3=st.tabs(["Maths","GK","Science"])
    
    #add maths questions
    with tab1:
        
        st.subheader("Upload your maths questions...")
        # Read the existing JSON data from the file

        with open('quiz_maths.json', 'r') as file:
            existing_maths_data = json.load(file)

            # Modify the Python object by adding new data

        q=st.text_input("enter your question")
        a=st.text_input("first choice")
        b=st.text_input("Second choice")
        c=st.text_input("third choice")
        d=st.text_input("forth choice")
        ca=st.text_input("enter the correct answer:")

        new_maths_data = {
            "question": q,
            "choices": ["",a,b,c,d],
            "correct_answer": ca
            }
        submitted=st.button("submit")
            
        if submitted:
            question_check=0
            maths_quiz_data = load_quiz_data('quiz_maths.json')
            for i,question in enumerate(maths_quiz_data):
                if new_maths_data["question"] in question["question"]:
                    question_check=question_check+1
                else:   
                    pass 
            if question_check==0:    
                    
                
                existing_maths_data.append(new_maths_data)
                st.info("your question has added successfully")

                    

                    
                        # Write the updated Python object back to the JSON file
                with open('quiz_maths.json', 'w') as file:
                        json.dump(existing_maths_data, file, indent=4)
            else:            
                st.warning("question already exists")
    
    with tab2:
        
        st.subheader("Upload your GK questions...")
        # Read the existing JSON data from the file

        with open('quiz_questions gk.json', 'r') as file:
            existing_gk_data = json.load(file)

            # Modify the Python object by adding new data

        q=st.text_input("enter your question",key="m1")
        a=st.text_input("first choice",key="m2")
        b=st.text_input("Second choice",key="m3")
        c=st.text_input("third choice",key="m4")
        d=st.text_input("forth choice",key="m5")
        ca=st.text_input("enter the correct answer:",key="m6")

        new_gk_data = {
            "question": q,
            "choices": ["",a,b,c,d],
            "correct_answer": ca
            }
        submitted=st.button("submit",key="m7")
            
        if submitted:
            question_check=0
            maths_quiz_data = load_quiz_data('quiz_maths.json')
            for i,question in enumerate(maths_quiz_data):
                if new_gk_data["question"] in question["question"]:
                    question_check=question_check+1
                else:   
                    pass 
            if question_check==0:    
                    
                
                existing_gk_data.append(new_gk_data)
                st.info("your question has added successfully")

                    

                    
                        # Write the updated Python object back to the JSON file
                with open('quiz_question gk.json', 'w') as file:
                        json.dump(existing_gk_data, file, indent=4)
            else:            
                st.warning("question already exists")
    with tab3:
        
        st.subheader("Upload your science questions...")
        # Read the existing JSON data from the file

        with open('quiz_science.json', 'r') as file:
            existing_science_data = json.load(file)

            # Modify the Python object by adding new data

        q=st.text_input("enter your question",key="s1")
        a=st.text_input("first choice",key="s2")
        b=st.text_input("Second choice",key="s3")
        c=st.text_input("third choice",key="s4")
        d=st.text_input("forth choice",key="s5")
        ca=st.text_input("enter the correct answer:",key="s6")

        new_science_data = {
            "question": q,
            "choices": ["",a,b,c,d],
            "correct_answer": ca
            }
        submitted=st.button("submit",key="s7")
            
        if submitted:
            question_check=0
            science_quiz_data = load_quiz_data('quiz_maths.json')
            for i,question in enumerate(science_quiz_data):
                if new_maths_data["question"] in question["question"]:
                    question_check=question_check+1
                else:   
                    pass 
            if question_check==0:    
                    
                
                existing_science_data.append(new_science_data)
                st.info("your question has added successfully")

                    

                    
                        # Write the updated Python object back to the JSON file
                with open('quiz_science.json', 'w') as file:
                        json.dump(existing_science_data, file, indent=4)
            else:            
                st.warning("question already exists")