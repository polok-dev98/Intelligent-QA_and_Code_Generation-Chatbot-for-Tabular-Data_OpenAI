#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import sys
import os
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
# OpenAI API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

df = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Flask route for uploading CSV file
@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    global df
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    return {"status": "success"}

@app.route('/generate_chart', methods=['POST'])
def generate_chart_api():
    user_query = request.form['query']

    df.columns = df.columns.str.strip().str.lower()

    print(df)
    prompt = f"""
    You are an expert in generating python code for statistical chart like bar, pie, histogram, scatter from a pandas dataframe.
    now your task is to generate python code for statistical chart from given dataframe based on english questions and save this image to a filder named  static folder with the name output.
    also the python should not have the line: "df = pd.read_csv('data.csv')" and "plt.show()"
    and always 'xticks' rotation will be vertical
    The given pandas DataFrame name is df 
    now generate Python code from the df dataframe based on english question

    For example :
     For example 1 :
     english query : generate code for pie chart of gender distribution
     python code :  gender_counts = df['gender'].value_counts()
                    # Plotting a Pie Chart
                    plt.figure(figsize=(12, 16))
                    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
                    plt.title('Distribution of Gender Among Students')
                    plt.savefig('.static/output.png')

     For example 2 :
     english query : generate python code for histogram of age based on name
     python code :  # Plotting the histogram
                    plt.figure(figsize=(12, 16))
    				plt.hist(df['Age'], bins=10, edgecolor='black')
                    plt.xticks(rotation='vertical')
    				plt.xlabel('Age')
    				plt.ylabel('Frequency')
    				plt.title('Histogram of Age based on Names')
    				plt.grid(True)
                    plt.savefig('.static/output.png')
    """
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Memorize the following CSV data:\n{df}"},
        {"role": "assistant", "content": "I have memorized the CSV data."},
        {"role": "assistant", "content": prompt},
        {"role": "user", "content": user_query}
    ]
    # Get completion

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=0.2
    )
    generated_code = completion.choices[0].message.content
    print(generated_code)

    def remove_first_and_last_lines(input_string):
        # Split the string into lines
        lines = input_string.split('\n')

        # Check if there are more than two lines
        if len(lines) >= 2:
            # Remove the first and last lines
            lines = lines[1:-1]

        # Join the remaining lines back into a string
        result_string = '\n'.join(lines)

        return result_string

    generated_code = remove_first_and_last_lines(generated_code)
    generated_code = generated_code.replace("`", "")
    generated_code = generated_code.replace("python", "")
    generated_code = generated_code
    print(generated_code)

    # Execute the generated Python code
    try:
        exec(generated_code)
    except Exception as e:
        print(f"Error executing the generated code: {e}")

    # Return success response
    return {"status": "success"}



@app.route('/generate_conversation', methods=['POST'])
def generate_conversation():
    user_query = request.form['query1']

    df.columns = df.columns.str.strip().str.lower()

    print(df)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Memorize the following CSV data:\n{df}"},
                    {"role": "assistant", "content": "I have memorized the CSV data."},
                    {"role": "user", "content": user_query}
                ],
        temperature=0.2
    )
    chat = completion.choices[0].message.content
    print(chat)
    return jsonify({"status": "success", "chat": chat})

if __name__ == '__main__':
    app.run(debug=True)
