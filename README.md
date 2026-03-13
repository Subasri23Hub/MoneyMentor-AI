#  MoneyMentor AI !

### Your Personal AI Financial Advisor

MoneyMentor AI is an intelligent **AI-powered financial advisor** built with **Streamlit** and **Google Gemini**.
It helps users analyze their **income, expenses, and savings**, visualize financial patterns, and receive **personalized financial guidance** for better money management.

Designed as a **modern fintech-style dashboard**, this application combines **data visualization** and **generative AI** to make financial planning simple and interactive.

---

##  Features

*  **Financial Dashboard**
  Track monthly income, expenses, and potential savings instantly.

*  **Budget Visualization**
  Interactive pie chart showing expense vs savings distribution.

*  **AI Financial Advisor**
  Ask questions about budgeting, saving strategies, or beginner investments.

*  **Personalized Insights**
  Gemini AI analyzes user input and provides tailored financial suggestions.

*  **Professional UI**
  Clean fintech-inspired interface with a modern Streamlit layout.

*  **Real-time Responses**
  AI responses generated instantly with a "Thinking..." indicator.

---

##  Tech Stack

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| **Python**            | Core programming language      |
| **Streamlit**         | Web application framework      |
| **Google Gemini API** | AI financial advice generation |
| **Plotly**            | Interactive financial charts   |
| **Pandas**            | Data processing                |

---

##  Project Structure

```
MoneyMentor-AI
│
├── chatbotapp.py        # Main Streamlit application
├── prompts.py           # AI prompt engineering
├── requirements.txt     # Project dependencies
├── .gitignore           # Ignored files
│
└── .streamlit
    └── secrets.toml     # API keys (not uploaded to GitHub)
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/MoneyMentor-AI.git
cd MoneyMentor-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Configure API Key

Create the folder:

```
.streamlit
```

Inside it create:

```
secrets.toml
```

Add your Gemini API key:

```
GEMINI_API_KEY = "your_api_key_here"
```

---

##  Run the Application

```bash
streamlit run chatbotapp.py
```

Your app will open at:

```
http://localhost:8501
```

---

##  Example Use Cases

* Understand monthly spending habits
* Discover ways to increase savings
* Get beginner-friendly investment suggestions
* Ask financial questions in natural language

---

## Future Improvements

*  Financial health score
*  Chat-style AI conversation interface
*  Expense categorization analytics

---

## Author

Developed by **Subasri B**

---

## License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
