import bs4
from urllib.parse import urljoin
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import asyncio
import aiohttp




#Global variable
ref_link=[]
def url_join(url):
    global ref_link
    ref_link = [urljoin(url, link) if not link.startswith("http") else link for link in ref_link]

async def fetch_page(session,url:str): #used in #used in scrape_element function and summarize_as
    async with session.get(fr"{url}") as response:
        return await response.text()

async def scrape_element(session, url, tag):
    global ref_link
    head = []
    para = []
    image = []
    content = await fetch_page(session=session, url = url)
    soup = bs4.BeautifulSoup(content,"html.parser")
    tags = soup.select(f"{tag}")

    for elements in tags:
        h2 = elements.select("h2")
        p = elements.select("p")
        img = elements.select('img[src]')
        ##check if both tags present extract iff <=> both present
        if h2 and p:
            head.append(h2[0].getText())
            para.append(p[0].getText())
            ref_link.append(elements.get('href'))
            if img:
                image.append(img[1]['src'])
            else:
                image.append("https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")

    url_join(url=url)

    sum_news =  await summarize(ref_link)

    return zip(head, para, image, sum_news)

def foo():
    pass

async def summarize(link_list): #used in scrape_element function
    summaries = []
    async with aiohttp.ClientSession() as session:
        try:
            for x in link_list:
                response = await fetch_page(session, x) #throws error code 200 why?

                if not response:
                    summaries.append(f"No content returned from {x}.")
                    continue

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

                    summaries.append(summary_sentences)
                else:
                    summaries.append("Summary not available.")  # If no article found
        except Exception as e:
            summaries.append(f"Some Error Occured at url = {x} error ---> {e}")

        return summaries


async def main():
    url = 'https://bbc.com'
    async with aiohttp.ClientSession() as session:
        news = await scrape_element(session=session,url=url,tag="a")
        context = {
            "news" : news
        }
        return context


# async def summarize_as(link_list): #used in scrape_element function
#     summaries = []
#     async with aiohttp.ClientSession() as session:
#         for url in link_list:
#             summary_result = "Failed to summarize"  # Default message
#             try:
#                 # Fetch the page content asynchronously
#                 response = await fetch_page(session, url)
#                 nest_soup = bs4.BeautifulSoup(response, "html.parser")
#                 nest_para = nest_soup.select('article')  # 'article' tag should be in lowercase
#
#                 if nest_para:  # Ensure there is an article tag
#                     full_news = nest_para[0].findAll('p')
#
#                     # Extract the text from all paragraphs
#                     news = [x.getText().strip() for x in full_news if x.getText().strip()]
#
#                     if news:
#                         # Merge all paragraphs into a single string
#                         text = " ".join(news)
#
#                         # Summarize the merged text
#                         parser = PlaintextParser.from_string(text, Tokenizer("english"))
#                         summarizer = TextRankSummarizer()
#                         summary = summarizer(parser.document, 5)  # Summarize into 5 sentences
#
#                         # Convert the summarized sentences into a single string
#                         summary_sentences = [str(sentence) for sentence in summary]
#                         summary_result = " ".join(summary_sentences)
#                     else:
#                         summary_result = "No text found for summarization."
#                 else:
#                     summary_result = "No article content found."
#             except Exception as e:
#                 summary_result = f"Failed to summarize for {url}: {str(e)}"  # More specific error message
#
#             summaries.append(summary_result)  # Append the result for this URL
#
#     return summaries



# def head_function():
#     head = []
#     para = []
#     image = []
#     global ref_link
#     url = "https://www.bbc.com/"
#     response = Req.get(url).text
#     soup = bs4.BeautifulSoup(response, "html.parser")
#     tag_a = soup.select('a')
#
#     for elements in tag_a:
#         h2 = elements.select("h2")
#         p = elements.select("p")
#         img = elements.select('img[src]')
#
#         if h2 and p:
#             head.append(h2[0].getText())
#             para.append(p[0].getText())
#             ref_link.append(elements.get('href'))
#
#             if img:
#                 image.append(img[1]['src'])
#             else:
#                 image.append("https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")
#
#
#     ref_link = [urljoin(url, link) if not link.startswith("http") else link for link in ref_link]
#
#     x = summarize(ref_link)
#     # Combining news and summaries
#     news = zip(head, para, image, x) #shall be untouched
#
#     context = {
#         "news_items": news
#     }
#     return context





