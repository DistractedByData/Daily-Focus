# Daily Focus
DailyFocus: Stay on track towards your goals with a morning check-in routine.
- **Focus on Goals**: Stay concentrated by defining success and preemptively tackling distractions.
- **Intuitive Interface**: Easily navigate the app thanks to its simple, user-friendly design.
- **User Details Saved**: Get started quickly with your daily check-in as the app conveniently saves your details.
- **Email Integration & Cross-Device Sharing**: Receive your DailyFocus prompts and answers directly in your inbox, and access them on any device. This keeps your goals and progress constantly in view, providing motivation and tracking progress at all times.

With DailyFocus, embrace a productive mindset, stay committed to your objectives, and steadily make strides towards your goals.

***Important:*** The app is for personal use only and saves credentials in an unencrypted file named "config.txt" in the application directory. Avoid using it on computers you don't own.

---

## Setting Up and Running the Daily Focus Application

Follow the steps below to set up and run the Daily Focus App.

### Step 1: Download and Extract Code

Firstly, download the code from GitHub as a zip file. Extract its contents to a directory of your choice.

### Step 2: Install Python

Make sure Python 3 is installed on your system. If Python isn't installed:
- Visit the official Python website at https://www.python.org.
- Follow the installation instructions suitable for your operating system.

### Step 3: Navigate to the Extracted Code Directory

Open a terminal or command prompt. Navigate to the directory where you extracted the code. For example, if you extracted the code to a folder named Daily-Focus on your desktop, use the following command on Mac OS:

```
cd ~/Desktop/Daily-Focus
```

### Step 4: Run the Application

Start the application by opening a terminal or command prompt and navigating to the directory containing the script. Run the following command:

```
python3 daily_focus.py
```
    Note: Depending on your system configuration, you may need to specify the full path to the Python executable or use the python3 command instead of python.

Upon launching, the application window will open, displaying a set of options for entering SMTP details, email credentials, and responding to prompts.

### Step 5: Input SMTP Details and Email Credentials

Input your SMTP server details and email credentials. You can do this by selecting the "SMTP Details" and "Email Details" options in the application interface and entering the information as prompted.

The details you need to provide include: SMTP server, SMTP port, email address, and email password. The application will automatically create a config.txt file in the same directory as the script and save these details for future use.

	Google/Gmail:
    SMTP server: smtp.gmail.com
    SMTP port (TLS): 587

	Microsoft Outlook/Hotmail:
    SMTP server: smtp.office365.com (if using Office 365) or smtp.live.com (for Hotmail accounts)
    SMTP port (TLS): 587

	Apple Mail (iCloud):
    SMTP server: smtp.mail.me.com
    SMTP port (TLS): 587

	Yahoo Mail:
    SMTP server: smtp.mail.yahoo.com
    SMTP port (TLS): 587


### Step 6: Interact with the Application

With the email and server details configured, you can now interact with the application's main features. Fill out the text entry fields by responding to the prompts, using the Tab key to navigate quickly between fields.

### Step 7: Send Your Responses by Email

After filling out all the fields, click the "Submit" button. If all fields are filled out correctly, the application will send an email containing your responses, using the SMTP server details specified in the config.txt file.

If any fields are empty, an error message will be displayed. You'll need to complete all fields before submitting again.


## Special Note:

If you have 2-step verification (2FA) enabled on your Gmail account, you will need to generate an App password to use as your password when setting up your SMTP server. Here are the steps to do so:

1. Go to your Google Account's settings.
2. Select Security.
3. Under "Signing in to Google," select 2-Step Verification.
4. At the bottom of the page, select App passwords.
5. Enter a name like "Daily Focus" to remember which app has access to the password.
6. Select Generate.
7. Copy and paste the app password into Daily Focus. The app password is the 16-character code that generates on your device.

You only need to set this up once because the password will save and load upon launching the Daily Focus app. Remember to keep this App password secure as it can bypass your 2FA settings.
