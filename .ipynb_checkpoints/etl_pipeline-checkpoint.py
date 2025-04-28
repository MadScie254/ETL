# etl_pipeline.py

import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from twilio.rest import Client

# ------------------------
# Email Alert Function
# ------------------------
def send_email_alert(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "danieleinstein1998@gmail.com"
    sender_password = "4805640@kmt"  # Gmail App Password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("📧 Email Alert Sent Successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# ------------------------
# WhatsApp Alert Function (Twilio)
# ------------------------
def send_whatsapp_alert(body):
    account_sid = "USd122d1bc28cba2bde526af8b46183ab9"
    auth_token = "your_twilio_auth_token"
    from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio Sandbox Number
    to_whatsapp_number = 'whatsapp:+254742007277'

    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=body,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )
        print("📲 WhatsApp Alert Sent Successfully.")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")

# ------------------------
# Logging Function
# ------------------------
def log_message(message):
    with open("etl_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# ------------------------
# ETL Functions
# ------------------------
def extract_data(csv_file):
    print("📥 Extracting data...")
    return pd.read_csv(csv_file)

def transform_data(df):
    print("🔄 Transforming data...")
    # Convert data types
    df['Year'] = df['Year'].astype(int)
    df['Active Agents'] = df['Active Agents'].astype(int)
    df['Total Registered Mobile Money Accounts (Millions)'] = df['Total Registered Mobile Money Accounts (Millions)'].astype(float)
    df['Total Agent Cash in Cash Out (Volume Million)'] = df['Total Agent Cash in Cash Out (Volume Million)'].astype(float)
    df['Total Agent Cash in Cash Out (Value KSh billions)'] = df['Total Agent Cash in Cash Out (Value KSh billions)'].astype(float)

    # Handle missing values
    df.fillna(0, inplace=True)

    # Feature Engineering: Create 'Date' column
    df['Date'] = pd.to_datetime(df['Month'] + ' ' + df['Year'].astype(str))
    return df

def load_data(df, database_file, table_name):
    print("💾 Loading data to database...")
    conn = sqlite3.connect(database_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def validate_load(database_file, table_name, expected_rows):
    print("🔍 Validating data...")
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    actual_rows = cursor.fetchone()[0]
    conn.close()
    return actual_rows == expected_rows

# ------------------------
# Visualization Function
# ------------------------
def visualize_data(df):
    print("📊 Generating plots...")
    if not os.path.exists('plots'):
        os.makedirs('plots')

    plt.figure(figsize=(10,6))
    plt.plot(df['Date'], df['Total Registered Mobile Money Accounts (Millions)'], marker='o')
    plt.title('Total Registered Mobile Money Accounts Over Time')
    plt.xlabel('Date')
    plt.ylabel('Accounts (Millions)')
    plt.grid(True)
    plt.savefig('plots/registered_accounts_trend.png')
    plt.close()

    plt.figure(figsize=(10,6))
    plt.plot(df['Date'], df['Total Agent Cash in Cash Out (Value KSh billions)'], marker='s', color='green')
    plt.title('Cash In/Out Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cash Value (KSh Billions)')
    plt.grid(True)
    plt.savefig('plots/cash_in_out_value_trend.png')
    plt.close()

    print("📈 Plots saved to 'plots/' folder.")

# ------------------------
# Main ETL Runner
# ------------------------
def main():
    csv_file = 'mobile_payments.csv'
    database_file = 'mobile_payments.db'
    table_name = 'mobile_payments'
    alert_email = 'recipient_email@example.com'

    try:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file '{csv_file}' not found.")

        df = extract_data(csv_file)
        df_cleaned = transform_data(df)
        load_data(df_cleaned, database_file, table_name)

        if validate_load(database_file, table_name, df_cleaned.shape[0]):
            print("✅ ETL Process Completed Successfully!")
            log_message("ETL succeeded and data validated.")
        else:
            raise ValueError("Validation failed: Row counts mismatch.")

        visualize_data(df_cleaned)

    except Exception as e:
        error_message = f"ETL Process Failed:\n{str(e)}"
        print(f"❌ {error_message}")
        log_message(f"ETL Failed: {str(e)}")
        send_email_alert(
            subject="🚨 ETL Process Failed!",
            body=error_message,
            to_email=alert_email
        )
        send_whatsapp_alert(f"🚨 ETL Failed: {str(e)}")

if __name__ == "__main__":
    main()
