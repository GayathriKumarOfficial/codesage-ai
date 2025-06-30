# 🧠 CodeSageAI – Offline Code Explainer & Debugger

CodeSageAI is a lightweight offline tool to **explain and debug Python code** using a clean Streamlit interface.  
It uses Python’s built-in `ast` module to explain code structure and `pyflakes` to detect syntax or logical errors — all **without using any online API or internet**.

---

## 📸 Output Screenshots

Screenshots are available inside the `output_screenshot/` folder.

-  Example of code explanation
-  Example of debug output

---

## 📁 Folder Structure

codesageAI/
├── app.py # Streamlit UI (main app)
├── explainer.py # Code explanation using AST
├── debugger.py # Bug detection using pyflakes
├── requirements.txt # Python dependencies
├── output_screenshot/ # Output screenshots
└── README.md # Project documentation

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://https://github.com/GayathriKumarOfficial/codesage-ai.git
cd codesage-ai


---

## 📦 Install Dependencies

Before running, make sure you have Python 3.8 or above installed.

Install required libraries:
```bash
pip install -r requirements.txt
or manually
pip install streamlit pyflakes

---

## 🚀 Launch the Application
streamlit run app.py

---

## 💡 Tech Stack
| Technology    | Purpose                                                           |
| ------------- | ----------------------------------------------------------------- |
| **Python**    | Main language used to build the application                       |
| **Streamlit** | Builds the web-based interface quickly from Python scripts        |
| **AST**       | Python module to parse code and analyze structure for explanation |
| **Pyflakes**  | Static code analysis tool to find bugs like undefined variables   |

---

## 🖥️ Features
✅ Paste Python code into the editor
✅ Click "Explain" to get code logic explanation
✅ Click "Debug" to find syntax/semantic issues
✅ Completely offline, no internet or API usage

---
## 🔮 Future Enhancements

Add syntax highlighting, file upload support, offline ML-based explanation, and smart bug fix suggestions to improve analysis depth and usability.

---


## License

This project is open-source and free to use. Modify it as needed for your personal or professional projects.

---

## 🤝 Contributions

Feel free to fork and contribute. Open a pull request with your suggestions.

---

## 📩 Contact

For queries: [gayathrikumarofficial@example.com]
LinkedIn:[www.linkedin.com/in/gayathrikumarofficial]


