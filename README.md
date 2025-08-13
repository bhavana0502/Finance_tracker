# Finance_tracker
Personal Finance Tracker is a Python-based desktop application that helps users manage their income and expenses. Built with Tkinter and ttkbootstrap for a modern interface, it allows users to set monthly and category budgets, track transactions, view spending summaries with charts, and toggle between light/dark themes. 
1. Project Title & Short Description
# 💰 Personal Finance Tracker
A Python-based desktop application to manage income, expenses, budgets, and visualize spending patterns with charts.
2. Features
## 🚀 Features
- Add, edit, and delete transactions
- Set monthly and category budgets
- View spending summaries with pie charts
- Dark mode toggle
- Monthly rollover savings
- Search transactions by keyword
- Export transactions to CSV
3. Technologies Used (brief or detailed)
  ## 🛠 Technologies Used
- **Python 3** – Core programming language
- **Tkinter** – GUI framework for desktop applications
- **ttkbootstrap** – Modern theming for Tkinter
- **Matplotlib** – For expense pie charts
- **JSON** – Local data storage format
- **CSV** – For exporting transaction records
4. Installation & Run Instructions
  ## ⚙️ Installation & Run
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install dependencies:
   ```bash
   pip install ttkbootstrap matplotlib
Run the application:
python app.py

---

### **5. Project Structure**
```markdown
## 📂 Project Structure
finance-tracker/
├── src/
│   └── app.py
├── data/
│   ├── transactions.json
│   ├── budget.json
│   ├── category_budgets.json
│   ├── app_config.json
├── screenshots/
│   ├── main_menu.png
│   ├── add_transaction.png
│   ├── summary_chart.png
└── README.md
6. Screenshots
i added screenshots in documentation

You said:
im making an app of finance tracker so i have code  and all the files
ChatGPT said:
Got it — you’ve got the code and files ready for your finance tracker app.
Do you want help structuring and organizing the files, reviewing/debugging the code, or packaging it into a working app (like APK for mobile or executable for desktop)?

You said:
i have to run that code file in google collab so that i get the app
ChatGPT said:
Alright — if your finance tracker app’s code is in Python, we can run it in Google Colab, but here’s the catch:

Google Colab can easily run backend or processing code, but it can’t directly launch a local app window or a full GUI like you would on your computer.
If your app is built with:

Streamlit, Flask, or FastAPI → you can run it in Colab and access it through a public link (via something like ngrok or localtunnel).

Tkinter, PyQt, or desktop-only GUIs → won’t work in Colab, but you can adapt them to web frameworks if you want it online.

If you give me:

The type of app (Streamlit, Flask, Tkinter, etc.)

Your main code file

I can give you the exact Colab commands so you can run it and open your finance tracker in a browser.

Is your finance tracker a web app or a desktop GUI?

You said:
i want to run that file in google collab
ChatGPT said:
Okay, then let’s set it up so you can run your finance tracker in Google Colab.
But first I need to know what type of app code you have — because the steps are different.

Here’s how it works depending on the app type:

App Type	Works in Colab?	How to Run
Streamlit	✅ Yes	Install streamlit, run it, and use ngrok to get a public link
Flask / FastAPI	✅ Yes	Install flask, run server, use ngrok for link
Tkinter / PyQt / Desktop GUI	❌ Not directly	Needs converting to a web-based app
Pure Python (no GUI)	✅ Yes	Just run cells in Colab
If you share the main .py file code (or at least the first 20–30 lines), I can give you the exact Colab setup so your app runs and you get a live link.

Is your finance tracker made with Streamlit, Flask, or something else?

You said:
i will shre uh the file
ChatGPT said:
Perfect 👍
Send me the file (or paste the code), and I’ll walk you through running it on Google Colab so you can get the live finance tracker app link.

You said:
app.py
Python
ChatGPT said:
Your app.py uses Tkinter (a desktop GUI library), which means it won’t run directly in Google Colab — Colab doesn’t support desktop windows.
If you try, it’ll give an error like TclError: no display name and no $DISPLAY environment variable.

You have two options:

Option 1 – Run Locally (Easiest)

Install Python (if you don’t have it).

Install the dependencies:

pip install ttkbootstrap matplotlib
Save your app.py and run:

python app.py
This will open the Personal Finance Tracker window on your computer.

Option 2 – Make it Colab-Compatible (Needs changes)
You’d have to convert it into a web app using something like Streamlit or Flask.
That way, you can run it in Colab and open it via a link in your browser.

Since your current code is fully Tkinter-based, if you want to run it in Colab without rewriting, it’s not possible. But if you’re okay with adapting it to Streamlit, I can convert your Tkinter UI into a browser-based interface so it works in Colab.

Do you want me to rewrite your app in Streamlit so it runs in Colab? That’s the only way to make it accessible online.

You said:
python means wat should i download?
ChatGPT said:
When I say Python, I mean the Python programming language interpreter — the software that runs .py files like your app.py.

To run your finance tracker on your computer, you’ll need:

1️⃣ Download & Install Python

Go to the official site: https://www.python.org/downloads/

Click "Download Python 3.x.x" (latest version, e.g., Python 3.12).

During installation, tick the box that says “Add Python to PATH” (very important!) before clicking Install.

2️⃣ Open a Command Prompt / Terminal

Windows: Press Win + R, type cmd, hit Enter.

Mac: Open Terminal from Applications → Utilities.

3️⃣ Install required libraries
In the terminal, run:

pip install ttkbootstrap matplotlib
4️⃣ Run your app
Go to the folder where your app.py is saved and run:

python app.py
This will open your Personal Finance Tracker window.

If you want, I can give you step-by-step instructions with screenshots so you can install Python and run your app without confusion.
Do you want me to prepare that guide for you?

You said:
can i do in idle?
ChatGPT said:
Yes ✅ — you can absolutely run your finance tracker in IDLE, and it might be the easiest option for you.

Here’s how you can do it:

1️⃣ Install Python (includes IDLE)
Go to https://www.python.org/downloads/

Download the latest Python 3.x.x version.

While installing, tick ✔ "Add Python to PATH" before clicking Install.

IDLE will be installed automatically along with Python.

2️⃣ Install extra libraries
Open Command Prompt (Windows) or Terminal (Mac).

Run:

pip install ttkbootstrap matplotlib
(This installs the UI styling library and charts support.)

3️⃣ Open your app in IDLE
Right-click on your app.py file → Open with → IDLE (Python GUI).

In IDLE, click Run → Run Module (or press F5).

The Personal Finance Tracker window will open. 🎯

If you want, I can give you a zero-confusion guide with step-by-step screenshots so you can set up Python + IDLE and run your file in one go.
Do you want me to make that for you?

You said:
idle is already installed
ChatGPT said:
Perfect 👍 — if IDLE is already installed, you’re halfway there.

You just need to:

1️⃣ Install the missing libraries
IDLE doesn’t come with ttkbootstrap or matplotlib, so you’ll have to install them.

Open Command Prompt (Windows) or Terminal (Mac).

Run:

pip install ttkbootstrap matplotlib
If you have multiple Python versions, you might need:

python -m pip install ttkbootstrap matplotlib
2️⃣ Open your app.py in IDLE
Right-click your app.py → Open with → IDLE (Python GUI)

Or open IDLE, click File → Open… and choose app.py.

3️⃣ Run the app
In IDLE, go to Run → Run Module (or press F5).

Your Personal Finance Tracker window should appear.

Do you want me to give you the exact Command Prompt commands so you can just copy-paste and make it work? That way, you won’t need to guess.

You said:
how to open command prompt in window
ChatGPT said:
On Windows, you can open Command Prompt in a few ways — here’s the easiest method:

Method 1 – Using Search
Press the Windows key on your keyboard (the one with the 🪟 logo).

Type cmd.

Click Command Prompt in the search results.

Method 2 – Using Run
Press Windows + R on your keyboard.

Type:

cmd
Press Enter — Command Prompt will open.

Once Command Prompt is open, you can type:

pip install ttkbootstrap matplotlib
and press Enter to install the libraries for your app. ✅

Do you want me to give you the exact step-by-step for running your app after this so you can see it in IDLE?

You said:
'pip' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\bhavana sherolla>python -m pip install ttkbootstrap matplotlib
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
ChatGPT said:
Got it — your error means Python isn’t installed (or not set up in PATH), so Windows can’t find it.

Since you already have IDLE, I suspect Python is installed but via the Microsoft Store or in a way that doesn’t add it to PATH.

Here’s what you should do to fix it:

Step 1 – Check Your Python Installation
Press Windows + R

Type:

idle
If IDLE opens, go to the menu Help → About IDLE — it will show the Python version (e.g., Python 3.11.4).

Step 2 – Find Python’s Location
In IDLE, open the Shell (the first window that appears).

Type:

import sys
sys.executable
Press Enter — it will show the full path of Python (e.g., C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe).

Step 3 – Install the Packages
In Command Prompt, type (replacing the path with your actual one):

"C:\path\to\python.exe" -m pip install ttkbootstrap matplotlib
Example:

"C:\Users\Bhavana\AppData\Local\Programs\Python\Python311\python.exe" -m pip install ttkbootstrap matplotlib
Once that works, you can go back to IDLE → Run your app (F5) and your Personal Finance Tracker will open. ✅

If you want, I can write the exact command for you once you give me the path that sys.executable shows in your IDLE.
Do you want to check that path now?

You said:
idle is not showing in window r
ChatGPT said:
Ah, that means IDLE might not actually be installed — maybe you had it on another computer before, or it was uninstalled when Python got removed.

On Windows, IDLE only comes when you install Python from python.org, not from the Microsoft Store.
Right now your PC doesn’t seem to have Python properly installed, which is why pip and python don’t work.

Here’s how to fix it:
1️⃣ Download Python (with IDLE included)

Go to https://www.python.org/downloads/

Click the yellow “Download Python 3.x.x” button.

Run the installer.

2️⃣ IMPORTANT: Tick “Add Python to PATH”

On the first install screen, you’ll see Add Python 3.x to PATH — tick this box before clicking “Install Now”.

3️⃣ After installation

Press Windows + R, type:

idle
and hit Enter — IDLE should open.

Or in Command Prompt, type:

python --version
and you should see something like Python 3.12.5.

4️⃣ Install your required libraries
In Command Prompt, run:

pip install ttkbootstrap matplotlib
Once that’s done, you can open your app.py in IDLE and press F5 — the Finance Tracker window will appear. 🎯

Do you want me to give you a full step-by-step with screenshots for installing Python + IDLE on Windows so you can follow without confusion?

You said:
can u show me the video
ChatGPT said:
Here’s a helpful video that walks you through installing Python on Windows and ensuring IDLE is included and works properly:


Once you've watched it, here’s a quick summary of the steps demonstrated:

Download the Python installer from the official site.

Make sure to check the box labeled “Add Python to PATH” before clicking "Install Now" — this ensures python and pip commands work in Command Prompt.

Complete the installation, then test by running:

python --version
Open IDLE easily via the Start menu.

Use Command Prompt to install your needed libraries:

pip install ttkbootstrap matplotlib
Finally, open your app.py in IDLE and press F5 (or go to Run → Run Module) to launch your finance tracker!

Would you like a similar tutorial video showing how to install and run the same using Command Prompt, too?

You said:
i installed python
ChatGPT said:
Great 🎉 — now you’re ready to set up the libraries and run your finance tracker.

Here’s what to do next:

1️⃣ Open Command Prompt
Press Windows + R, type:

cmd
and hit Enter.

2️⃣ Check Python installation
In Command Prompt, type:

python --version
You should see something like:

Python 3.12.5
If you see that, it’s working.

3️⃣ Install required libraries
In Command Prompt, run:

pip install ttkbootstrap matplotlib
4️⃣ Run your app in IDLE
Right-click your app.py file → Open with → IDLE (Python GUI)

In IDLE, press F5 or go to Run → Run Module.

Your Personal Finance Tracker window will open. ✅

Do you want me to give you a ready-to-copy Command Prompt command so you don’t have to navigate to the correct folder manually? That’ll make running it easier.

You said:
Uploaded image
explain deliverables of my app in github point to point
ChatGPT said:
From your screenshot, here’s a point-by-point breakdown of the GitHub deliverables for your finance tracker app:

📦 Code Repository (GitHub)
Upload your complete codebase

Create a GitHub repository for your project.

Include all project folders such as:

/src → your Python scripts (e.g., app.py).

/data → any JSON/CSV files used for storing transactions, budgets, etc.

/screenshots → images of your app’s UI for documentation.

Write clean, modular code

Keep code organized into functions and classes (your current Tkinter code already does this well).

Avoid unnecessary code repetition.

Maintain clear file/folder structure.

Add comments

Use inline comments to explain tricky parts of the code.

Add docstrings ("""...""") at the start of functions and classes to describe what they do.

📝 Documentation (README.md)
Your README.md should explain your project so someone on GitHub can understand and run it easily.
Include:

App purpose and features

Example: “This Personal Finance Tracker helps users manage expenses, set budgets, and visualize spending with charts.”

Mention features like category budget tracking, dark mode toggle, monthly rollover, keyword search, etc.

Technologies used

Example: Python, Tkinter, ttkbootstrap, Matplotlib, JSON for data storage.

Setup / Run instructions

Step-by-step guide for installing Python, required libraries, and running app.py.

Mention:

pip install ttkbootstrap matplotlib
python app.py
Sample screenshots

Add images from the /screenshots folder showing your app in action (main menu, adding transactions, charts, etc.).

If you want, I can write your full README.md in a clean GitHub-ready format so you just paste it into your repository.
Do you want me to make that for you?

You said:
description about my project in short
ChatGPT said:
Here’s a short description you can use for your project:

Personal Finance Tracker is a Python-based desktop application that helps users manage their income and expenses. Built with Tkinter and ttkbootstrap for a modern interface, it allows users to set monthly and category budgets, track transactions, view spending summaries with charts, and toggle between light/dark themes. Data is stored locally in JSON files, ensuring easy use without external databases.

You said:
i need a documemtation of my project according to the requirement
ChatGPT said:
Got it ✅
I’ll prepare a full documentation (README.md) for your Personal Finance Tracker exactly according to the requirements in your screenshot:

Personal Finance Tracker
📌 App Purpose & Features
The Personal Finance Tracker is a Python-based desktop application designed to help users manage and monitor their personal finances efficiently.
It offers an intuitive interface built with Tkinter and ttkbootstrap for a modern look, enabling users to:

Add, edit, and delete transactions with amount, category, date, and notes.

Set monthly budgets and receive alerts if exceeded.

Track spending by category with visual pie charts.

Toggle between Light and Dark Mode.

Automatically reset monthly records with rollover savings calculation.

Search transactions by keyword for quick access.

Export transactions to CSV for backup or sharing.

🛠 Technologies Used
Python 3 – Core programming language.

Tkinter – GUI framework for desktop applications.

ttkbootstrap – Modern theming for Tkinter widgets.

Matplotlib – For generating expense pie charts.

JSON – For storing user transactions, budgets, and configurations.

CSV – Export format for transactions.

⚙️ Setup & Run Instructions
1. Install Python
Download from python.org

During installation, check the box "Add Python to PATH".

2. Install Required Libraries
Open Command Prompt and run:

pip install ttkbootstrap matplotlib
3. Run the Application
Download or clone the repository.

Navigate to the folder containing app.py.

Run:

python app.py
The Personal Finance Tracker window will open.

📂 Project Structure
finance-tracker/
│
├── src/
│   └── app.py                 # Main application code
│
├── data/
│   ├── transactions.json      # Stores all transactions
│   ├── budget.json             # Monthly budget data
│   ├── category_budgets.json   # Per-category budget data
│   ├── app_config.json         # Theme and rollover settings
│
├── screenshots/
│   ├── main_menu.png           # Main menu screenshot
│   ├── add_transaction.png     # Add transaction window
│   ├── summary_chart.png       # Pie chart of expenses
│
└── README.md                   # Documentation
📸 Sample Screenshots
(Place screenshots of your app in the /screenshots folder and display them here)

Main Menu:

Add Transaction:

Summary Chart:

🌟 Bonus Features Implemented
✅ Budget tracking by category

✅ Dark Mode toggle

✅ Monthly reset with rollover savings

✅ Transaction search by keyword

📢 LinkedIn Post
Create a short 2–3 min demo video showing:

Opening the app.

Adding transactions.

Setting budgets.

Viewing charts and using search.

Post on LinkedIn, tag @infobharatinterns, and use relevant hashtags.

If you want, I can also prepare a ready-to-use GitHub README file with proper Markdown formatting and placeholders for screenshots so you can just upload it with your project.
Do you want me to prepare that Markdown file now?

You said:
s i need github read me file4
ChatGPT said:
Alright ✅
Here’s your GitHub-ready README.md for the Personal Finance Tracker — fully formatted in Markdown so you can upload it directly to your repository.

# 💰 Personal Finance Tracker

## 📌 App Purpose & Features
The **Personal Finance Tracker** is a Python-based desktop application that helps users manage and monitor their income and expenses.  
It provides an intuitive and modern interface built with **Tkinter** and **ttkbootstrap**, offering the following features:

- ➕ **Add, edit, and delete transactions** with amount, category, date, and notes.  
- 💵 **Set monthly budgets** and get alerts if exceeded.  
- 📊 **Track spending by category** with visual pie charts.  
- 🌙 **Dark Mode toggle** for better viewing experience.  
- 🔄 **Monthly reset with rollover savings calculation**.  
- 🔍 **Search transactions** by keyword for quick access.  
- 📂 **Export transactions to CSV** for backup or sharing.  

---

## 🛠 Technologies Used
- **Python 3** – Core programming language  
- **Tkinter** – GUI framework for desktop applications  
- **ttkbootstrap** – Modern theming for Tkinter widgets  
- **Matplotlib** – For generating expense pie charts  
- **JSON** – For storing transactions, budgets, and configuration  
- **CSV** – Export format for transactions  

---

## ⚙️ Setup & Run Instructions

### **1. Install Python**
- Download from [python.org](https://www.python.org/downloads/)  
- During installation, **check** the box **"Add Python to PATH"**  

### **2. Install Required Libraries**
Open Command Prompt and run:  
```bash
pip install ttkbootstrap matplotlib
3. Run the Application
Download or clone this repository

Navigate to the folder containing app.py

Run:

python app.py
The Personal Finance Tracker window will open

📂 Project Structure
finance-tracker/
│
├── src/
│   └── app.py                 # Main application code
│
├── data/
│   ├── transactions.json      # Stores all transactions
│   ├── budget.json            # Monthly budget data
│   ├── category_budgets.json  # Per-category budget data
│   ├── app_config.json        # Theme and rollover settings
│
├── screenshots/
│   ├── main_menu.png          # Main menu screenshot
│   ├── add_transaction.png    # Add transaction window
│   ├── summary_chart.png      # Pie chart of expenses
│
└── README.md                  # Documentation
📸 Sample Screenshots
(Place screenshots of your app in the /screenshots folder and display them here)

Main Menu:

Add Transaction:

Summary Chart:

🌟 Bonus Features Implemented
✅ Budget tracking by category

✅ Dark Mode toggle

✅ Monthly reset with rollover savings

✅ Transaction search by keyword

📢 LinkedIn Post
Create a short 2–3 min demo video showing:

Opening the app

Adding transactions

Setting budgets

Viewing charts and using search

Post on LinkedIn, tag @infobharatinterns, and use hashtags like #Python and #BharatIntern.


---

If you want, I can also **add your screenshots** and **push this to a GitHub repository** for you so it’s fully ready.  
Do you want me to prepare the **screenshots + GitHub upload guide** next?
You said:
 i need a documemtation of my project according to the requirement
ChatGPT said:
Got it ✅
I’ll prepare the complete project documentation according to the requirements shown in your screenshot — including all the points they expect you to submit.

📄 Project Documentation – Personal Finance Tracker
1. App Purpose & Features
The Personal Finance Tracker is a desktop application that helps users manage their income, expenses, and savings effectively.
It provides an easy-to-use interface for adding, editing, and deleting transactions, setting monthly budgets, and visualizing spending patterns.

Key Features:

Add, edit, and delete transactions with details like amount, category, date, and note.

Set monthly budgets and receive alerts when they are exceeded.

Set budgets for each spending category (e.g., Food, Transport, Bills).

Track expenses with a visual pie chart using Matplotlib.

Toggle between light and dark themes.

Automatically reset monthly data with rollover savings calculation.

Search transactions by keyword.

Export transactions to CSV for backup.

2. Technologies Used
Python 3 – Programming language.

Tkinter – GUI framework for desktop applications.

ttkbootstrap – Modern theming for Tkinter widgets.

Matplotlib – For expense charts.

JSON – For local data storage.

CSV – For exporting transactions.

3. Setup / Run Instructions
Step 1 – Install Python
Download from python.org

During installation, check "Add Python to PATH".

Step 2 – Install Dependencies
Open Command Prompt and run:

pip install ttkbootstrap matplotlib
Step 3 – Run the Application
Download or clone the project repository.

Open Command Prompt and navigate to the folder containing app.py.

Run:

python app.py
The Personal Finance Tracker window will open.

4. Project Structure
finance-tracker/
│
├── src/
│   └── app.py                 # Main application code
│
├── data/
│   ├── transactions.json      # Transaction history
│   ├── budget.json            # Monthly budget data
│   ├── category_budgets.json  # Category-wise budget data
│   ├── app_config.json        # Theme and rollover settings
│
├── screenshots/
│   ├── main_menu.png          # Main menu view
│   ├── add_transaction.png    # Add transaction form
│   ├── summary_chart.png      # Expense pie chart
│
└── README.md                  # Documentation
5. Sample Screenshots
(Store these in /screenshots folder and link them in README)

Main Menu:

Add Transaction:

Summary Chart:

6. Bonus Features Implemented
✅ Budget tracking by category
✅ Dark Mode toggle
✅ Monthly reset with rollover savings
✅ Transaction search by keyword

7. LinkedIn Post Instructions
Record a 2–3 min demo video showing:

Opening the app

Adding transactions

Setting monthly & category budgets

Viewing expense summary and charts

Using search & theme toggle

Post the video on LinkedIn, tag @infobharatinterns, and use hashtags:
#Python #BharatIntern #FinanceTracker

If you want, I can now format this as a proper GitHub README.md so you can directly upload it with your project repository.
Do you want me to do that next?

You said:
in a word document as im preparing the document
ChatGPT said:
I’ve created your project documentation in Word format.
You can download it here:

📄 Personal_Finance_Tracker_Documentation.docx

This file contains all required sections — purpose, features, technologies, setup steps, structure, screenshots, bonus features, and LinkedIn post instructions. 

You said:
2. Technologies Used
- Python 3 – Programming language.
- Tkinter – GUI framework for desktop applications.
- ttkbootstrap – Modern theming for Tkinter widgets.
- Matplotlib – For expense charts.
- JSON – For local data storage.
- CSV – For exporting transactions.  more discriptive
ChatGPT said:
I’ve updated the Technologies Used section to be more descriptive.
You can download the revised documentation here:

📄 Personal_Finance_Tracker_Documentation_Updated.docx 

You said:
wat should in put in read me
ChatGPT said:
For your Personal Finance Tracker project, your README.md on GitHub should include these main sections so anyone visiting your repo knows what your app does, how to use it, and how to run it.

Here’s the structure you should follow:

📄 README.md Structure
1. Project Title & Short Description
# 💰 Personal Finance Tracker
A Python-based desktop application to manage income, expenses, budgets, and visualize spending patterns with charts.
2. Features
## 🚀 Features
- Add, edit, and delete transactions
- Set monthly and category budgets
- View spending summaries with pie charts
- Dark mode toggle
- Monthly rollover savings
- Search transactions by keyword
- Export transactions to CSV
3. Technologies Used (brief or detailed)
## 🛠 Technologies Used
- **Python 3** – Core programming language
- **Tkinter** – GUI framework for desktop applications
- **ttkbootstrap** – Modern theming for Tkinter
- **Matplotlib** – For expense pie charts
- **JSON** – Local data storage format
- **CSV** – For exporting transaction records
4. Installation & Run Instructions
## ⚙️ Installation & Run
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Install dependencies:
   ```bash
   pip install ttkbootstrap matplotlib
Run the application:

python app.py

---

### **5. Project Structure**
```markdown
## 📂 Project Structure
finance-tracker/
├── src/
│   └── app.py
├── data/
│   ├── transactions.json
│   ├── budget.json
│   ├── category_budgets.json
│   ├── app_config.json
├── screenshots/
│   ├── main_menu.png
│   ├── add_transaction.png
│   ├── summary_chart.png
└── README.md
6. Screenshots
i added screenshots  
7. Bonus Features (Optional)
## 🌟 Bonus Features
- Budget tracking by category
- Monthly reset with rollover savings
- Dark Mode toggle
- CSV export for reports
