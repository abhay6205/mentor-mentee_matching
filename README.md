# 🤝 Mentor–Mentee Matching System

An **AI-powered recommendation system** that helps mentees find the most suitable mentors based on **specialization**, **tech stack**, and **experience** using **TF-IDF**, **K-Means clustering**, and **cosine similarity**.

---

## 📌 Project Structure

mentor-mentee_matching/
│── README.md # Project documentation
│── code.py # Main Python program (CLI-based)
│── mentor_data.xlsx # Dataset of mentors


📝 *Right now the project runs through the terminal (CLI). Web interface (Streamlit) can be added later.*

---

## 🌟 Features

- 🔍 Recommends top mentors based on similarity score  
- 🧠 ML-powered matching: TF-IDF + K-Means + cosine similarity  
- 📊 Cluster-based grouping of mentors  
- 📎 Displays mentor details (name, title, tech stack, reviews, LinkedIn etc.)  
- 🖥 Simple CLI interface — no need for login or installation of heavy software  

---

## 🧠 How the Algorithm Works

| Stage | Technique Used |
|--------|---------------|
| Profile representation | TF-IDF Vectorization |
| Experience addition | Numeric feature concatenation |
| Feature scaling | StandardScaler |
| Mentor grouping | K-Means Clustering |
| Mentor ranking | Cosine Similarity |

🔁 Recommends the **top 3 most relevant mentors** based on the mentee’s input.

---

## 🚀 Getting Started (Run the Project)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abhay6205/mentor-mentee_matching.git
cd mentor-mentee_matching


2️⃣ Install Required Libraries
pip install pandas numpy scikit-learn openpyxl

3️⃣ Ensure Dataset Exists

Make sure mentor_data.xlsx is present in the same directory as code.py.

4️⃣ Run the Program
python code.py

You will be asked:

Desired Specialization: 
Preferred Tech Stack:
Preferred Mentor Experience Level:

Then the top mentors will be displayed one by one with:
Name
Professional Title
Specialization
Tech Stack
Experience Level
LinkedIn Link
Reviews
Similarity Score

📁 Dataset Requirements

Your Excel file should contain columns like:

| Column Name       | Example                                                 |
| ----------------- | ------------------------------------------------------- |
| userName          | Rahul Sharma                                            |
| professionalTitle | Senior Backend Developer                                |
| specialization    | Web Development, Microservices                          |
| techStack         | Java, SpringBoot, SQL                                   |
| levelOfExperience | 6                                                       |
| linkedin          | [https://linkedin.com/in/](https://linkedin.com/in/)... |
| combined_reviews  | Very helpful and supportive mentor                      |

🔮 Future Improvements

✔ Convert CLI into a Streamlit Web App
✔ Add sentiment analysis to reviews
✔ Deploy publicly via Streamlit Cloud
✔ Allow mentees to contact mentors directly from the interface
✔ Add database support instead of Excel

👤 Author

Abhay Kumar
🔗 GitHub: https://github.com/abhay6205

⭐ If this project helped you, don’t forget to star the repository!
