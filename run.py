import pandas as pd
import openpyxl
import os
import datetime

# 現在時刻のフォルダの作成
folder_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs("./outputfile/{}".format(folder_name), exist_ok=True)

# 入力excelファイルの読み込み
INPUT_PATH = "./inputfile/excel_sample.xlsx"
df = pd.read_excel(INPUT_PATH, engine="openpyxl")

# 1行ずつ処理
for index, row in df.iterrows():
    number = row["項番"]
    question = row["質問"]
    answer = row["回答"]
    text = f"""\
#項番
{number}
    
#質問
{question}
    
#回答
{answer}
"""

    # 出力ファイルの作成
    file_name = "./outputfile/{}/{}.txt".format(folder_name, number)
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(text)