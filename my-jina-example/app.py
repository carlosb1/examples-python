import os
from jina.flow import Flow


def print_topk(resp, sentence):
    dialog = ''
    print(f"{str(resp.search.docs)}")
    for d in resp.search.docs:
        print(f'Here is the news that we found for: {sentence}')
        for idx, match in enumerate(d.matches):
            score = match.score.value
            if score < 0.0:
                continue

            character = match.meta_info.decode()

            if len(match.chunks) == 0:
                continue
            elif len(match.chunks) > 0:
                dialog = match.chunks[0].text
            print(character + ' ' + dialog)
            print('n')


def index(num_docs, max_docs, data_file):
    f = Flow().load_config('flow-index.yml')
    with f:
        f.index_lines(filepath=data_file, batch_size=8,
                      size=max_docs)


def query(num_docs, top_k):
    f = Flow().load_config('flow-query.yml')
    with f:
        while True:
            text = input('please type a sentence: ')
            if not text:
                break

            def ppr(x):
                return print_topk(x, text)
            f.search_lines(lines=[text, ], output_fn=ppr, top_k=top_k)


def dryrun(num_docs):
    f = Flow().load_config('flow-index.yml')
    with f:
        f.dry_run()


def main():
    num_docs = 5
    top_k = 5
    max_docs = 500
    data_file = './data/news_articles.csv'
    index(num_docs, max_docs, data_file)
    query(num_docs, top_k)


if __name__ == '__main__':
    main()
