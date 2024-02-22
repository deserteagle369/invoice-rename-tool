import requests
import base64
import urllib.parse
import pandas as pd
import os
import re
import tkinter as tk
from tkinter import filedialog
import configparser

# 创建配置解析器
config = configparser.ConfigParser()
# 读取配置文件
config.read('config.ini')

# 从配置文件获取百度API的访问信息
APP_ID = config['BaiduAPI']['APP_ID']
API_KEY = config['BaiduAPI']['API_KEY']
SECRET_KEY = config['BaiduAPI']['SECRET_KEY']


def select_directory():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_selected = filedialog.askdirectory()  # 弹出文件夹选择对话框
    return folder_selected

# 百度OCR API配置
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"

# 获取access_token
def get_access_token():
    params = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET_KEY
    }
    response = requests.post(TOKEN_URL, params=params)
    if response:
        return response.json().get('access_token')

# 处理PDF文件
def process_pdf(file_path, access_token, invoice_details):
    with open(file_path, 'rb') as f:
        pdf_content = base64.b64encode(f.read()).decode()
    
    params = urllib.parse.urlencode({"pdf_file": pdf_content})
    request_url = f"{OCR_URL}?access_token={access_token}"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    
    if response:
        result = response.json()
        # 提取发票信息
        if 'words_result' in result:
            words_result = result['words_result']
            invoice_date = re.sub(r'年|月', '-', words_result['InvoiceDate']).replace('日', '')
            commodity_names = " ".join([item['word'] for item in words_result.get('CommodityName', [])]) or "none"
            new_filename = f"{words_result.get('InvoiceCodeConfirm', 'none')} {words_result.get('InvoiceNumConfirm', 'none')} {invoice_date} {words_result.get('AmountInFiguers', 'none')} {words_result.get('SellerName', 'none')}.pdf".replace("none", "none")
            new_path = os.path.join(os.path.dirname(file_path), new_filename)
            os.rename(file_path, new_path)

            invoice_details.append({
                "发票代码": words_result.get('InvoiceCodeConfirm', 'none'),
                "发票号码": words_result.get('InvoiceNumConfirm', 'none'),
                "开票日期": invoice_date,
                "项目名称": commodity_names,
                "价税合计": words_result.get('AmountInFiguers', 'none'),
                "销售方名称": words_result.get('SellerName', 'none')
            })

# 处理指定目录下的所有PDF文件
def process_invoices(directory):
    access_token = get_access_token()
    invoice_details = []

    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            process_pdf(file_path, access_token, invoice_details)

    # 将提取的信息保存到Excel文件中
    df = pd.DataFrame(invoice_details)
    excel_path = os.path.join(directory, '发票明细.xlsx')
    df.to_excel(excel_path, index=False)

# 示例调用
#directory = "D:\\Documents\\"  # 更新为实际的发票文件目录
directory = select_directory()
print("Selected directory:", directory)
process_invoices(directory)
