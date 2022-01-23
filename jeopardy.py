import pandas as pd
pd.set_option('display.max_colwidth', -1)
df=pd.read_csv('jeopardy.csv')
# This showing the number of Columns
print(df.columns)
df = df.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
print(df.columns)

def filter_df(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['Question'].apply(filter)]

filter_test = filter_df(df, ['king', 'England'])
print(filter_test)

df['Float Value'] = df['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

filtered = filter_df(df, ["King"])
print(filtered["Float Value"].mean())

def get_answer_counts(data):
  return data['Answer'].value_counts()

print(get_answer_counts(filtered))
