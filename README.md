# lexrank-summary
LexRank is an unsupervised approach to text summarization based on graph-based centrality scoring of sentences. The main idea is that sentences “recommend” other similar sentences to the reader. Thus, if one sentence is very similar to many others, it will likely be a sentence of great importance. The importance of this sentence also stems from the importance of the sentences “recommending” it. Thus, to get ranked highly and placed in a summary, a sentence must be similar to many sentences that are in turn also similar to many other sentences. This makes intuitive sense and allows the algorithms to be applied to any arbitrary new text.

This program analyses a dataset of news and summarizes it in accordance to our threshhold.
