# Mozilla Credits Email Sender

This script automates the process of sending batch emails using SMTP. It retrieves recipient email addresses from an Excel file, filters them based on specific criteria, and sends emails in batches to avoid SMTP limits.

## How It Works
1. The script reads email addresses from an Excel file.
2. It filters recipients where the **"Status"** column is marked as **"YES"**.
3. It sends emails in **BCC** to recipients in batches of 100 to avoid SMTP limits.
4. The script authenticates using an App Password for security.

## Required Parameters
To use this script, you need to provide the following details:

### SMTP Configuration
- **`sender_email`**: Your email address (e.g., `your-email@gmail.com`)
- **`sender_password`**: An **App Password** generated from your Google account (details below)
- **`smtp_server`**: SMTP server (default: `smtp.gmail.com`)
- **`smtp_port`**: SMTP port (default: `587`)

### Email Details
- **`recipients`**: A list of email addresses (fetched from the Excel file)
- **`subject`**: The subject of the email
- **`body`**: The main content of the email
- **`batch_size`**: The number of recipients per batch (default: `100`)

## Why Batch Size is 100?
Most SMTP servers (including Gmail) impose a limit on the number of recipients per email to prevent spam. The batch size of **100** ensures that the script complies with these limitations while maintaining efficiency. If you have more than 100 recipients, the script will send multiple emails in separate batches.

## How to Generate a Google App Password
Since Google restricts direct login via scripts, you must use an **App Password**:

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Sign in to your Google account.
3. Select **Mail** as the app and **Other (Custom Name)** for the device.
4. Click **Generate**, and copy the 16-character password.
5. Use this password in the script instead of your regular Gmail password.

## Running the Script
1. Install dependencies:
   ```sh
   pip install pandas openpyxl
   ```
2. Replace `your-email@gmail.com` and `your-app-password` in the script.
3. Run the script:
   ```sh
   python mail_dispatch.py
   ```

## Notes
- This script is specifically designed for the **Mozilla Credits** repository.
- Ensure that your **Excel file follows the correct format** with email addresses and a "Status" column.
- Modify the script if you need a different filtering condition.

For any issues or modifications, please contribute to the Mozilla Credits repo!

