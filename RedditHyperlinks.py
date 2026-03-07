import csv
import pandas as pd
import networkx as nx
import json
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("reddit.tsv", sep="\t")
    edges = df[['SOURCE_SUBREDDIT', 'TARGET_SUBREDDIT']]

    graph = nx.from_pandas_edgelist(edges, source='SOURCE_SUBREDDIT', target='TARGET_SUBREDDIT', create_using=nx.DiGraph())
    ranked = nx.pagerank(graph)
    nodes = sorted(ranked.items(), key=lambda x:x[1], reverse=True)[:10]
    nx.write_graphml(graph, "reddit.graphml")

    #utilized gephi, didn't see anything visually interesting

    #Will utilize matplotlib to visualize the top 10 subreddits by pagerank

    names = [x[0] for x in nodes]
    scores =[x[1] for x in nodes]

    plt.bar(names, scores)
    plt.xticks(rotation = 90)
    plt.title("Top 10 Subreddits by PageRank")
    plt.ylabel("PageRank Score")

    plt.show()
    return

if __name__ == "__main__":
    main()