import tweepy
from tweepy import OAuthHandler
import time
import csv



# @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def extract_tweet():
    consumer_key = 'kTP7Uog4vwlOl8RS5qvCr0GeU'
    consumer_secret = '5NpBZgTJex7TkdpDILoE6FC4qmO9WEvp6zE95qWovhwAplAo5x'
    access_token = '994133061049581568-FOKWPLkZTk0mdryAB6NfrGRyUB0VVSo'
    access_secret = 'dHEtPkQmhcMRexk50jq3UG17bGAEAuTWYzRDzYfPta62S'

    queries = ["diabetic", "legpain", "Insulin", "agave", "Antibiotics", "Diabetes", "publichealth",
               "Diabeticcardiomyopathy", "typeonediabetic", "typetwodiabetic", "LowCarb", "Ginger",
               "Glaucoma", "Vitamin_D", "GlucoseTolerance", "SugarFree", "Farxiga", "DiabetesWeek", "herbal_medicine",
               "insulintherapy", "CardiacEvents", "DiabeticsTreatment", "Healthyfood", "NaturalDrink", "HerballyPure",
               "diabeticRetinopathy", "Bloodsugar", "BloodGlucose", "diet", "DiabetesDiet", "fingermillet",
               "Type2diabetes", "healthychoices", "MDES2017", "selfcare", "insulinpen", "diabulimia"]

    since = "2019-06-20"
    until = "2019-06-27"
    index = 1
    limitation = 600
    file_name = "diabetics" + since + "_" + until + ".csv"

    csvFile = open(file_name, 'w', newline='', encoding='utf-8')
    for query in queries:
        try:
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret)
            api = tweepy.API(auth)

            for tweet in tweepy.Cursor(api.search, q='#'+query, since=since, until=until, tweet_mode='extended', lang="en").items(600):

                try:

                    csvWriter = csv.writer(csvFile)
                    csvWriter.writerow([query, tweet.user.screen_name, tweet.created_at, tweet.full_text, tweet.entities["media"][0]["media_url"]])
                    print(index)
                    index += 1

                    if index == limitation:
                        time.sleep(500)
                        index = 1
                        break

                except:
                    print("Doesn't have media!")
                    continue

        except tweepy.error.TweepError:
            csvFile.close()
            raise

    csvFile.close()


if __name__ == '__main__':
    extract_tweet()