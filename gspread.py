import gspread
from google.oauth2.service_account import Credentials

def upload_to_sheets(data, sheet):
    # 設置憑證和授權
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    # 帶入API key
    creds = Credentials.from_service_account_file(r'APIkey.json', scopes=scopes)

    client = gspread.authorize(creds)
    
    # 嘗試打開名為 'name' 的試算表，如果不存在則創建
    try:
        sheet = client.open('name')
    except gspread.SpreadsheetNotFound:
        sheet = client.create('name')
    
    # 嘗試獲取名為sheet的工作表，如果不存在則創建
    try:
        worksheet = sheet.worksheet(sheet)
    except gspread.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=sheet, rows="1000", cols="3")
    # 分享試算表的權限
    sheet.share('yourgmail@gmail.com', perm_type='user', role='writer')
   
   
    # 設置欄位標題(搭配下方測試)
    worksheet.update([['name', 'price', 'link']], 'A1:C1')
    
    # 準備數據以插入工作表(搭配下方測試)
    rows_to_insert = [[item['name'], item['price'], item['link']] for item in data]
    
    # 將數據插入工作表(搭配下方測試)
    worksheet.append_rows(rows_to_insert)


if __name__ == "__main__":
    data = [
        {'name': 'Product 1', 'price': 100, 'link': 'https://example.com/product1'},
        {'name': 'Product 2', 'price': 200, 'link': 'https://example.com/product2'},
        {'name': 'Product 3', 'price': 300, 'link': 'https://example.com/product3'}
    ]
    upload_to_sheets(data, 'test')

