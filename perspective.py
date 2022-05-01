from googleapiclient import discovery
import json

API_KEY = 'AIzaSyBy4qJESV2vU_7d-EmOvB70WdkJOm6QFd8'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1")

def analyse_text_req(text):
  analyze_request = {
    'comment': { 'text': 'friendly greetings from python' },
    'requestedAttributes': {'TOXICITY': {},'INSULT': {},'PROFANITY': {},'THREAT': {}}
  }

  response = client.comments().analyze(body=analyze_request).execute()

  toxic = response['attributeScores']['TOXICITY']['summaryScore']['value']
  insult = response['attributeScores']['INSULT']['summaryScore']['value']
  profanity = response['attributeScores']['PROFANITY']['summaryScore']['value']
  threat = response['attributeScores']['THREAT']['summaryScore']['value']

  return [toxic,insult, profanity, threat]
  # print(response)
  # print(response.attributeScores.TOXICITY.summaryScore.value)
  # print(json.dumps(response, indent=2))

  # response_score = client.comments().suggestscore(body=analyze_request).execute()
  # print(json.dumps(response_score, indent=2))

def check_prob(value):
  if value>0.7:
    return 1
  return 0

def analyse_yt_req(comments):
  toxic = 0
  insult = 0
  profanity = 0
  threat = 0

  for comment in comments:
    res = analyse_text_req(comment)
    toxic = toxic + check_prob(res[0])
    insult = insult + check_prob(res[1])
    profanity = profanity + check_prob(res[2])
    threat = threat + check_prob(res[3])

  toxic = (toxic/len(comments))*100
  insult = (insult/len(comments))*100
  profanity = (profanity/len(comments))*100
  threat = (threat/len(comments))*100

  return [toxic,insult, profanity, threat]


analyse_text_req("Hello you are a buffallo")
