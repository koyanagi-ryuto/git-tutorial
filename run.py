import pandas as pd
import openpyxl
import os
import datetime

# 現在時刻のフォルダの作成
folder_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs("./outputfile/{}".format(folder_name), exist_ok=True)

# 入力excelファイルの読み込み
input_path = "./inputfile/excel_sample.xlsx"
df = pd.read_excel(input_path, engine="openpyxl")

# 1行ずつ処理
for index, row in df.iterrows():
    number = row["項番"]
    question = row["質問"]
    answer = row["回答"]

    # 出力ファイルの作成
    file_name = "./outputfile/{}/{}.txt".format(folder_name, number)
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write("#項番\n")
        f.write("{}\n\n".format(number))
        f.write("#質問\n")
        f.write("{}\n\n".format(question))
        f.write("#回答\n")
        f.write("{}\n".format(answer))