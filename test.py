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