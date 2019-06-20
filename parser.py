"""
This file uses instaScrapper output for extracting hashtags and twitter file. Then, it combines them.
"""
import re
import pandas
from file_writer import writer

hashtags = dict()


def twitter_hashtag_extractor(file):
    with open(file, 'r') as f:
        text = f.read()
    twitter_hashtags = re.findall(r"#(\w+)", text)

    return list(set(twitter_hashtags))


def insta_hashtag_extractor(file):
    insta_hashtags = []
    data = pandas.read_csv(file, header=None)
    for item in data[5]:
        try:
            insta_hashtags += item.split(',')

        except:
            continue

    return list(set(insta_hashtags))


if __name__ == '__main__':

    twitter_address = 'Twitter/diabetics/allTweets.txt'
    insta_address = '../InstaScrapper/results.csv'
    output_address = 'Twitter/output.csv'

    # Call the extractors
    hashtags.update(twitter=twitter_hashtag_extractor(twitter_address))
    hashtags.update(insta=insta_hashtag_extractor(insta_address))
    print(hashtags)

    # Write the results to the file
    writer(output_address, hashtags)

    # except:
    #     print("please enter the correct address :) ")


