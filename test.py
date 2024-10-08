from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import bs4 , requests as Req
from urllib.parse import urljoin



# def summarize_text(text, sentence_count=5):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = TextRankSummarizer()
#     summary = summarizer(parser.document, sentence_count)
#     summary_sentences = [str(sentence) for sentence in summary]
#     return " ".join(summary_sentences)
#
#
# # Example usage:
# text = """
# Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals.
# Leading AI textbooks define the field as the study of intelligent agents.
# An intelligent agent is any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
# Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic cognitive functions that humans associate with the human mind.
# """
# summary = summarize_text(text)
# print("Summary:\n", summary)

#
# text = ""
# parser = PlaintextParser.from_string(text, Tokenizer("english"))
# summarizer = TextRankSummarizer()
# summary = summarizer(parser.document, 5)
# summary_sentences = [str(sentence) for sentence in summary]
# " ".join(summary_sentences)
#
#
#
#
# url = "https://www.bbc.com/"
# response = Req.get(url).text
# soup = bs4.BeautifulSoup(response, "html.parser")
# tag_a = soup.select('a')
# ref_link = []
# head = []
# para = []
# image = []
# for elements in tag_a:
#     h2 = elements.select("h2")
#     p = elements.select("p")
#     img = elements.select('img[src]')
#     if h2 and p:
#         ref_link.append(elements.get('href'))
#         head.append(h2[0].getText())
#         para.append(p[0].getText())
#         if img:
#             image.append(img[1]['src'])
#         else:
#             image.append(r"https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")
# # news = zip(head, para, image)
# for x in range(0,len(ref_link)):
#     if not ref_link[x].startswith("http"):
#         ref_link[x] = urljoin(url,ref_link[x])
#
#



#
# for x in ref_link:

# print(summary_sentences)
summaries = []
response = Req.get("https://www.bbc.com/news/articles/crl8e084r9yo").text
nest_soup = bs4.BeautifulSoup(response, "html.parser")
nest_para = nest_soup.select('article')  # 'article' tag should be in lowercase

if nest_para:  # Ensure there is an article tag
    full_news = nest_para[0].findAll('p')

    # Extract the text from all paragraphs
    news = [x.getText() for x in full_news]

    # Merge all paragraphs into a single string
    text = " ".join(news)

    # Summarize the merged text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 5)  # Summarize into 5 sentences

    # Convert the summarized sentences into a single string
    summary_sentences = [str(sentence) for sentence in summary]
    summary_sentences = " ".join(summary_sentences)
    # Store the summary in a dictionary
    con_text = {"summary": summary_sentences}

    summaries.append(summary_sentences)
else:
    summaries.append("Summary not available.")  # If no article found

# Final context with all summaries
context = {
    "data_sum": summaries
}

