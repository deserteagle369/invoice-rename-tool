import requests
import base64
import urllib.parse
import pandas as pd
import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import configparser

# 尝试从环境变量获取配置信息
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

if not all([APP_ID, API_KEY, SECRET_KEY]):
    # 配置信息不完整，尝试读取config.ini文件
    config_path = ".\\config.ini"
    # 假设已经有函数load_config来处理读取config.ini的逻辑
    # APP_ID, API_KEY, SECRET_KEY = load_config(config_path)
    
    if not all([APP_ID, API_KEY, SECRET_KEY]):
        # 如果配置信息仍然不完整，提示用户
        if not os.path.exists(config_path):
            print("配置文件不存在，正在创建...")
            # 可以复制 config.ini.example 为 config.ini
            example_path = 'config.ini.example'
            if os.path.exists(example_path):
                with open(example_path) as example, open(config_path, 'w') as config:
                    config.write(example.read())
                    root = tk.Tk()
                    root.withdraw()  # 隐藏主窗口
                messagebox.showerror("配置错误", f"请编辑 {config_path} 文件并填写相应的配置信息。")
            else:
                messagebox.showerror("配置模板文件缺失", f"请确保 config.ini.example 文件存在。")    
            exit(1)

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the Baidu API access information from the configuration file
APP_ID = config['BaiduAPI']['APP_ID']
API_KEY = config['BaiduAPI']['API_KEY']
SECRET_KEY = config['BaiduAPI']['SECRET_KEY']

# Function to select a directory
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Show the folder selection dialog
    return folder_selected

# Function to get the access token
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"
def get_access_token():
    print("Getting access token...")
    params = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET_KEY
    }
    response = requests.post(TOKEN_URL, params=params)
    if response:
        print("Access token received.")
        return response.json().get('access_token')
    else:
        print("Failed to retrieve access token.")
        return None

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

# Function to process a file for OCR
def process_file(file_path, access_token, invoice_details):
    print(f"Processing file: {file_path}")
    #with open(file_path, 'rb') as f:
        #file_content = base64.b64encode(f.read()).decode("utf8")
    #    file_content = base64.b64encode(f.read()).decode("utf8")
    #    if urlencoded:
    #        file_content = urllib.parse.quote_plus(content)
    content=get_file_content_as_base64(file_path,True)
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in ['.jpg', '.jpeg', '.png', '.bmp']:
        params = {"image": file_content}
    elif file_extension == '.pdf':
        params = {"pdf_file": file_content}
    elif file_extension == '.ofd':
        params = 'ofd_file='&content&'seal_tag=false'
    else:
        print(f"Unsupported file format: {file_path}")
        return

    params = urllib.parse.urlencode(params)
    headers = {
                "Accept": "application/json",
               'content-type': 'application/x-www-form-urlencoded'
                }
    request_url = f"{OCR_URL}?access_token={access_token}"
    response = requests.post(request_url, data=params, headers=headers)

    if response and response.status_code == 200:  # 假设成功的响应状态码为200:
        result = response.json()
        print(f"Response received for file: {file_path}")
        # Process the OCR result
        if 'words_result' in result:
            words_result = result['words_result']
            # 示例提取逻辑，应根据实际API响应结构调整
            invoice_date = re.sub(r'年|月', '-', words_result['InvoiceDate']).replace('日', '')  # 开票日期格式化
            total_amount = words_result.get('AmountInFiguers', 'none')  # 价税合计
            seller_name = words_result.get('SellerName', 'none')  # 销售方名称
            invoice_code = words_result.get('InvoiceCodeConfirm', 'none')  # 发票代码
            invoice_number = words_result.get('InvoiceNumConfirm', 'none')  # 发票号码

            # 构造新的文件名
            # new_filename = f"{invoice_date} {total_amount} {seller_name} {invoice_code} {invoice_number}{file_extension}"
            # new_path = os.path.join(os.path.dirname(file_path), new_filename)
            # os.rename(file_path, new_path)
            # print(f"File renamed to: {new_filename}")

            invoice_details = {
                "开票日期": invoice_date,
                "价税合计": total_amount,
                "销售方名称": seller_name,
                "发票代码": invoice_code,
                "发票号码": invoice_number
            }
            # Call rename_file here
            file_renamed = rename_file(file_path, invoice_details)
            if file_renamed:
                print(f"File renamed successfully: {file_path}")
                return True
            else:
                print(f"Failed to rename file: {file_path}")
            return False
        else:
            print(f"No words result in response for file: {file_path}")
            return False
    else:
        print(f"Failed to get a valid response for file: {file_path}")
        return False

# Function to save details to an Excel file
def save_to_excel(details, directory):
    print(f"Saving details to Excel file in directory: {directory}")
    df = pd.DataFrame(details)
    excel_path = os.path.join(directory, 'invoice_details.xlsx')
    df.to_excel(excel_path, index=False)
    print(f"Details saved to {excel_path}")

# Function to rename the file
def rename_file(original_path, new_details):
    # Your code to rename the file based on new details
    # 构建新文件名
    # Extract file extension from original_path
    _, file_extension = os.path.splitext(original_path)    
    new_filename = f"{new_details['开票日期']} {new_details['价税合计']} {new_details['销售方名称']} {new_details['发票代码']} {new_details['发票号码']}{file_extension}"
    new_path = os.path.join(os.path.dirname(original_path), new_filename)  
    # 检查目标文件是否已存在
    if os.path.exists(new_path):
        print(f"Warning: Target file {new_path} already exists. Skipping.")
        return False  # 或者考虑添加一个唯一后缀以避免重名

    try:
        os.rename(original_path, new_path)
        print(f"File renamed to: {new_filename}")
        return True
    except FileExistsError:
        print(f"Error: Cannot rename {original_path} because the target file already exists.")
    except Exception as e:
        print(f"Error: Failed to rename file due to {e}")

    return False
    print(f"Rename Done")

# Function to process all files in the directory
def process_invoices(directory):
    access_token = get_access_token()
    if not access_token:
        print("No access token available. Exiting.")
        return

    files_processed = 0
    files_successfully_processed = 0

    invoice_details = []

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png', '.bmp')):
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")
            files_processed += 1
            response = process_file(file_path, access_token, invoice_details)
            if response:
                files_successfully_processed += 1
    print(f"Total files processed: {files_processed}")
    print(f"Files successfully processed: {files_successfully_processed}")            

    save_to_excel(invoice_details, directory)

# Main execution
if __name__ == "__main__":
    directory = select_directory()
    if directory:
        print(f"Selected directory: {directory}")
        process_invoices(directory)
    else:
        print("No directory selected. Exiting.")
input("Press any key to exit...")