import os

def read(filenames):
    for filename in filenames:
        yield filename, open(filename).read()

def words(input):
    for filename, data in input:
        yield filename, len(data.split())


def filter(input, pattern):
    for item in input:
        if item.endswith(pattern):
            yield item


if __name__ == "__main__":
    stream1 = filter(os.listdir('.'), '.py')
    stream2 = read(stream1)
    stream3 = words(stream2)

    for item in stream3:
        print(item)


