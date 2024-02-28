#sample of image
import base64
import urllib
import requests

API_KEY = "Vp4CabaD4MIpYGzs5FMMWSHY"
SECRET_KEY = "bcQqlhicNFTZkByO7lsw59sj9hDYSwvf"

def main():
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token=" + get_access_token()
    
    # image 可以通过 get_file_content_as_base64("C:\fakepath\2019-12-17 70000.00 华沃通讯(上海)有限公司 3100182130 77181184.jpg",True) 方法获取
    payload='image=%2F9j%2F4AAQSkZJRgABAQEBLAEsAAD%2F2wBDAAEBAQEBAQEBAQEBA&seal_tag=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

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

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()

#sample of pdf
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

#sample of ofd
import base64
import urllib
import requests

API_KEY = "Vp4CabaD4MIpYGzs5FMMWSHY"
SECRET_KEY = "bcQqlhicNFTZkByO7lsw59sj9hDYSwvf"

def main():
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token=" + get_access_token()
    
    # ofd_file 可以通过 get_file_content_as_base64("C:\fakepath\031001900511_84911760.ofd",True) 方法获取
    payload='ofd_file=UEsDBBQAAAAIAHmmeFFSgvYrMgIAAG&seal_tag=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

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

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
