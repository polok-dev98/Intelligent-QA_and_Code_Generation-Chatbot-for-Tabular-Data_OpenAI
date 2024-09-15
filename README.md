# Chart Generation and Data Interaction Web Application

This project is a web application designed for generating various statistical charts (bar, pie, histogram, scatter) based on user-uploaded CSV data. It also includes a conversational AI feature using OpenAI's GPT-4 model for generating Python code snippets based on natural language input related to data queries. The application is built using Flask, with OpenAI's API for conversation and code generation, and utilizes Pandas for data handling and Matplotlib/Seaborn for visualization.

![image](https://github.com/user-attachments/assets/1d717c29-c7b4-4738-a2bd-44c4f6d69d99)

## Folder Structure

- **main.py**: The main Flask application.
- **templates/**: Contains the HTML template for the web interface.
- **static/**: Stores generated chart images and other static files (e.g., logos, screenshots).
- **Dockerfile**: A Docker configuration for containerizing the application.
- **.env**: Stores environment variables such as the OpenAI API key.
- **r.txt**: Requirements file listing all necessary Python packages.
- **README.md**: Project documentation.

## Installation

To run this project locally, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/polok-dev98/Intelligent-QA_and_Code_Generation-Chatbot-for-Tabular-Data_OpenAI.git
cd project_folder
```

## Installation

### Install the required dependencies:
```bash
pip install -r r.txt
```

### Set up your OpenAI API key:
Create a .env file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key
```

### Run the Flask application:
```bash
python main.py
```
### Open your web browser and go to:
```bash
http://localhost:5000
```

- **Upload a CSV file. </br>
- **Interact with the application by either generating a chart from the CSV data or asking data-related queries.

## How It Works

- **CSV Upload**: Users upload a CSV file via the web interface.
- **Chart Generation**: Users ask the application to generate specific statistical charts (e.g., pie chart of gender distribution) based on natural language input.
- **OpenAI Integration**: For more complex queries, the application communicates with the GPT-4 API to generate Python code to perform the requested operation.
- **Result Display**: The resulting charts or outputs are saved in the `static` folder and displayed to the user.

## Example

### Example Queries:
- "Generate a pie chart of the gender distribution."
- "Generate a histogram of ages from the dataset."
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgments
- OpenAI for the GPT-4 API.
- Flask for the web framework.
- Matplotlib and Seaborn for data visualization.


