from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def handler(context, event):
    body = event.body.decode('utf-8')
    context.logger.debug_with('Analyzing', 'sentence', body)
    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(body)

    return str(score)

