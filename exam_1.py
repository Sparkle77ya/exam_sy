import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置日期和货币代号
date = sys.argv[1]
currency_code = sys.argv[2]

# 初始化 Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无界面模式
service = Service('path_to_chromedriver.exe')  # 需要替换为你本地的 Chrome WebDriver 路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 访问中国银行外汇牌价网站
url = f"https://www.boc.cn/sourcedb/whpj/index_{date}.html"
driver.get(url)

# 查找货币代号对应的现汇卖出价
try:
    currency_table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "publish"))
    currency_rows = currency_table.find_elements_by_tag_name("tr")

    for row in currency_rows:
        cells = row.find_elements_by_tag_name("td")
        if len(cells) >= 8 and currency_code in cells[0].text:
            selling_rate = cells[7].text
            break
    else:
        selling_rate = "未找到对应货币的汇率"

except Exception as e:
    selling_rate = f"发生异常：{str(e)}"

# 将结果写入 result.txt 文件
with open("result.txt", "w") as file:
    file.write(selling_rate)

# 关闭 WebDriver
driver.quit()
