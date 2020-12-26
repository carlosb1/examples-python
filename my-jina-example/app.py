from jina import Flow
f = (Flow().add(name='dummyEncoder', uses='mwu.yml'))

with f:
    f.dry_run()
