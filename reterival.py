# Reranker model ko load mat karein (RAM bachane ke liye)
def rerank(question, docs):
    # Sirf pehle se nikalay gaye top documents return karein
    # Is se koi extra model load nahi hoga aur speed fast ho jayegi
    return docs[:5] 
