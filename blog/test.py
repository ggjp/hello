# 辞書型のデータ
dict_data = [{'001': '在庫A', '数量': 100.0, '単価': 50.0}, 
             {'002': '在庫B', '数量': 200.0, '単価': 60.0}, 
             {'003': '在庫C', '数量': 300.0, '単価': 70.0}]

# 辞書を展開して、商品コードとそれ以外のデータを分ける
expanded_data = []
for d in dict_data:
    for key, value in d.items():
        if isinstance(value, str):
            product_code = key
            product_name = value
        else:
            other_data = {key: value}
    expanded_data.append({**{'商品コード': product_code, '在庫詳細': product_name}, **other_data})

# DataFrameに変換
df3 = pd.DataFrame(expanded_data)

print(df3)
# df1, df2 の結合
merged_df = pd.merge(df1, df2, on='商品コード', how='left')

# df3との結合
final_df = pd.merge(merged_df, df3, on='商品コード', how='left')

print(final_df)
