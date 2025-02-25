import urllib3
import re


def create_word_list():
    # Initialize urllib3 PoolManager
    http = urllib3.PoolManager()

    # Fetch the text file
    url = "https://www.wordfrequency.info/samples/lemmas_60k.txt"
    response = http.request("GET", url)

    # Decode the response
    text = response.data.decode("utf-8")

    # Extract words (assuming words are separated by whitespace or newlines)
    words = re.findall(r"\b[a-zA-Z']+\b", text)

    exclude_list = ['https', 'Excel']

    words = set([word for word in words if (len(word) == 5) and (word not in exclude_list)])

    return words


