import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():


    url = utext.get('1.0','end').strip()

    article=Article(url)

    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')


    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

#Gui for user

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1920x1080')

#title
tlabel = tk.Label(root,text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=180)
title.config(state='disabled', bg='#dddddd')
title.pack()

#author
alabel = tk.Label(root,text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=180)
author.config(state='disabled', bg='#dddddd')
author.pack()

#publication
plabel = tk.Label(root,text='Publication')
plabel.pack()

publication = tk.Text(root, height=1, width=180)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

#summary
slabel = tk.Label(root,text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=180)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

#sentiment analysis
stlabel = tk.Label(root,text='Sentiment Analysis')
stlabel.pack()

sentiment = tk.Text(root, height=1, width=180)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

#url
ulabel = tk.Label(root,text='URL')
ulabel.pack()

utext = tk.Text(root, height=1, width=180)
utext.pack()

#Summary button
btn = tk.Button(root, text='Summarize',command=summarize)
btn.pack()

root.mainloop()