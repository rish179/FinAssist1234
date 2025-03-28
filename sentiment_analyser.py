from unittest.mock import sentinel

import requests
import json

class Sentiment_Analyser:
    def analyse(self, news_list=" "):

        #set up your azure endpoint and api key
        endpoint = "https://staru-m8pt35cw-eastus2.cognitiveservices.azure.com/"
        api_key = "54Rcm5Ua2knlWmENeoQyFYdqDnNvmMBtBCFxWjLdZXRPMKPJDxghJQQJ99BCACHYHv6XJ3w3AAAAACOGqIOR"
        deployment_name = "gpt-4"
        api_version = "2024-10-01-preview"

        # the text to analyse
        text = "Stock prices for Tesla surged after the announcement of a new battery technology."

        # construct the request headers and body
        headers ={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        body = {
            "model": "gpt-4",
            "messages": [
                {
                    "role": "user",
                    "content": f"Two word sentiment(hold, buy, sell) of this stock-related news: '{text}'. Is it positive, negative, or neutral?"
                } for text in news_list
            ],
            "max_tokens" : 10
            # "stream" : True
        }
        sentiment = ""

        try:
            #send the request to the API
            response = requests.post(f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}",
                                     headers=headers,
                                     data=json.dumps(body))
            # Check if the request was successful (Status Code: 200-299)
            response.raise_for_status()
            print(response.text)

            # # check the success and extract the response
            # if response.status_code == 200:
            #     result = response.json()
            #     sentiment = result["choices"][0]["message"]["content"]

            # Check if response contains data before calling .json()
            if response.text.strip():
                response_data = response.json()  # Convert response to JSON
                print("Response:", response_data)
                sentiment = response_data["choices"][0]["message"]["content"]
            else:
                print("Error: Empty response from API")

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            print(f"Error {response.status_code}: {response.text}")

        except json.JSONDecodeError:
            print("Error: API response is not valid JSON")


        return sentiment

