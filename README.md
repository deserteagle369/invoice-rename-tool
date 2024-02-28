# 发票识别与重命名工具

该工具使用百度API进行发票识别，自动提取发票信息，并根据发票信息重命名PDF和图片文件。
申请百度AI的接口，每个月可领免费额度2000次，方法请自行百度。
https://cloud.baidu.com/product/ocr_receipts/vat_invoice

## 特性

- 支持多种文件格式，包括PDF、JPG、PNG等。
- 自动从发票中提取关键信息，如发票号码、开票日期、销售方名称等。
- 根据提取的信息重命名文件，便于管理和归档。

## 下载和运行

### 对于非Python用户

如果您不熟悉Python或不希望安装Python环境，我们提供了一个独立的`.exe`文件，您可以直接下载并运行这个程序，无需进行额外的安装或配置。

1. 访问GitHub仓库的[Releases页面](https://github.com/deserteagle369/invoice-rename-tool/releases)。
2. 下载最新版本的`.exe`文件。
3. 双击下载的文件以运行程序。

### 对于Python用户

如果您熟悉Python，您可以按照下面的安装指南来运行源代码。

#### 前提条件

- Python 3.6或更高版本。
- 依赖库：`requests`、`pandas`、`tkinter`（通常Python自带）、`configparser`。

#### 安装步骤

1. **确保Python已安装**：在命令行中运行`python --version`或`python3 --version`来检查Python版本。
2. **下载脚本**：从GitHub或其他提供的链接下载`invoice-rename.py`脚本及相关文件（如`config.ini`）。
3. **安装依赖库**：打开命令行工具，导航到脚本所在目录，运行以下命令安装所需的Python库：

   
`pip install requests pandas`

5. **配置API密钥**：在`config.ini`文件中填入你的百度API的`APP_ID`、`API_KEY`、`SECRET_KEY`。

## 使用指南

1. **启动脚本**：在命令行中导航到脚本所在目录，运行：
   
`python invoice-rename.py`

4. **选择文件夹**：在弹出的窗口中选择包含发票文件的文件夹。
5. **处理文件**：脚本将自动处理文件夹中的所有支持的发票文件，并根据发票信息进行重命名。

## 支持和反馈

如遇到任何问题或需要帮助，请通过以下方式联系我们：
- 邮箱：deserteagle369@163.com
- GitHub Issues：[https://github.com/deserteagle369/invoice-rename-tool]
