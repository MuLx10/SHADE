user = '81e26502-12d9-41ea-8733-20ae1b1e529e'
passw = 'lcNh5jcMesWJ'

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username=user,
    password=passw,
    url = 'https://gateway.watsonplatform.net/tone-analyzer/api')

def get_tone_json(text):
    # text = 'Team, I know that times are tough! Product '\
    #     'sales have been disappointing for the past three '\
    #     'quarters. We have a competitive product, but we '\
    #     'need to do a better job of selling it!'

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json')
    # print(tone_analysis)
    # print(json.dumps(tone_analysis, indent=2))
    # return json.loads(tone_analysis)
    return str(tone_analysis)
    return json.dumps(tone_analysis, indent=2)