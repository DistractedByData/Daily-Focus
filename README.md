# Daily Focus
DailyFocus: Stay on track towards your goals with a morning check-in routine.
- **Focus on Goals**: Stay concentrated by defining success and preemptively tackling distractions.
- **Intuitive Interface**: Easily navigate the app thanks to its simple, user-friendly design.
- **User Details Saved**: Get started quickly with your daily check-in as the app conveniently saves your details.
- **Email Integration & Cross-Device Sharing**: Receive your DailyFocus prompts and answers directly in your inbox, and access them on any device. This keeps your goals and progress constantly in view, providing motivation and tracking progress at all times.

With DailyFocus, embrace a productive mindset, stay committed to your objectives, and steadily make strides towards your goals.

***Important:*** The app is for personal use only and saves credentials in an unencrypted file named "config.txt" in the application directory. Avoid using it on computers you don't own.

---

## Setting Up and Running the Morning-Check-In-App

Follow the steps below to set up and run the Morning-Check-In-App.

### Step 1: Download and Extract Code

Firstly, download the code from GitHub as a zip file. Extract its contents to a directory of your choice.

### Step 2: Install Python

Make sure Python 3 is installed on your system. If Python isn't installed:
- Visit the official Python website at https://www.python.org.
- Follow the installation instructions suitable for your operating system.

### Step 3: Navigate to the Extracted Code Directory

Open a terminal or command prompt. Navigate to the directory where you extracted the code. For example, if you extracted the code to a folder named morning-check-in-app, use the following command:

```
cd /path/to/morning-check-in-app
```

### Step 4: Create a Configuration File

Before running the script for the first time, create a file named config.txt in the same directory as the script. Add your SMTP server details and email credentials, placing each item on a separate line in the following order: SMTP server, SMTP port, email address, email password.

Alternatively, run the script and use the "SMTP Details" and "Email Details" options in the application interface to input these details.

### Step 5: Run the Application

Having configured your SMTP server details and email credentials, run the application by executing the following command:
```
python3 daily_focus.py
```
	Note: Depending on your system configuration, you may need to specify the full path to the Python executable or use the python3 command instead of python.

### Step 6: Interact with the Application

The application window should open, displaying prompts and text entry fields. Fill out these fields with your responses to the prompts, using the Tab key to navigate between them.

### Step 7: Submit the Form

After filling out all the fields, click the "Submit" button. If all fields are filled out correctly, the application will send an email containing your responses, using the SMTP server details specified in the config.txt file.

If any fields are empty, an error message will be displayed. You'll need to complete all fields before submitting again.