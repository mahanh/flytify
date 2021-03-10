from flytekit import task


@task(cache_version="1", cache=True)
def reader(source_query: str) -> str:
    print(f"Reading source_query: {source_query}")
    return "source_uri"


@task(cache_version="1", cache=True)
def writer(target_uri: str) -> None:
    print(f"Writing target_uri: {target_uri}")
