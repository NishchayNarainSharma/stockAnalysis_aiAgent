from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text("NVIDIA latest news", region='wt-wt', safesearch='Moderate', timelimit='d')
    for result in results:
        print(result)

