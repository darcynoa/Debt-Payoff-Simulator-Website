<!-- @format -->

You're correct that setting up a virtual environment is a good practice, especially when working with Python and Flask. It helps isolate dependencies and makes it easier to manage different projects. Here’s a more detailed, step-by-step guide on how to run the app locally.

# Your go-to Debt Payment Strategy!

## 🚀 Overview

Welcome to the enhanced debt payoff simulation app! This project is a revamp of a Python-based tool originally developed in Google CoLab. The goal? 🎯 To make it super easy for you to simulate the best ways to pay off your debts—without ever touching Python or Google Sheets. We're adding a sleek Next.js front-end and integrating a Python Flask backend to handle all the heavy lifting.

## 🛠️ Tech Stack

- **Frontend:** Next.js ⚛️
- **Backend:** Python Flask 🐍
- **Styling:** Tailwind CSS 🎨
- **Animation:** GSAP (may change depending on needs) 🌠

## 📝 Progress

### ✅ Done

- Forked the original repo & set up Next.js
- Basic Flask API to connect Python script with the front-end

### 🚧 In Progress

- Building basic UI components 🧩
- API integration between Next.js and Flask 🔗
- Designing the full UI 🖼

### 🔜 Upcoming

- Finalize API integration
- Complete UI design & testing 🧪
- Deploy on Vercel & PythonAnywhere 🚀

## 🛠️ How to Run Locally

### 1. **Clone the Repo:**

Open your terminal and run the following commands to clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. **Set Up Python Virtual Environment (for Flask Backend):**

It’s recommended to set up a virtual environment to manage your Python dependencies. Here’s how to do it:

- **Create a virtual environment:**

  ```bash
  python3 -m venv venv
  ```

- **Activate the virtual environment:**

  - On **macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

  - On **Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **Install Python dependencies:**

  Once the virtual environment is active, install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

### 3. **Install Node.js Dependencies (for Next.js Frontend):**

In a separate terminal, navigate to the project directory if you haven’t already, and run:

```bash
npm install
```

This will install all the necessary Node.js packages required by the Next.js frontend.

### 4. **Run the Development Servers:**

You’ll need two terminals to run the Flask backend and the Next.js frontend simultaneously.

- **Terminal 1:** Start the Flask backend server:

  ```bash
  npm run flask-dev
  ```

- **Terminal 2:** Start the Next.js frontend server:

  ```bash
  npm run dev
  ```

### 5. **Access the Application:**

Open your web browser and navigate to [http://localhost:3000](http://localhost:3000) to see the application in action.

### 6. **Deactivate the Virtual Environment:**

Once you’re done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

## 🤝 Contributing

Want to help out? Check out the `CONTRIBUTING.md` to get started! 🎉

## 📄 License

This project is under the MIT License.

---

Stay tuned for more updates! 😊
