# Authours: Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS)
# Date: Jan 14th, 2023

import pandas as pd
import jellyfish as jf

def find_similar_name(match_name, limit=10):
    """
    Generate a random list of names that sound similar to a given user input name.
    
    Uses Match rating approach algorithm to determine similarity
      
    Parameters
    ----------
    match_name : string
        Name for comparison; output names will sound like this one 
    limit : int
        The number of names in the output list. (default = 10)
    Returns
    -------
    list:
        A name list containing random suggested similar names based on the given name.
    Examples
    --------
    >>> find_similar_name('Elizabeth', 5)
    >>> ['Elisabeth', 'Elliott', 'Ellsworth', 'Emmalynn', 'Ryley']
    """
    
    # Data loading and cleaning
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv"
    raw_df = pd.read_csv(url)
    raw_df = raw_df[raw_df["n"] >= 100] # Keep only names that had at least 100 births for a single gender in a single year
    unique_names = raw_df['name'].unique()
    unique_names = unique_names[unique_names != match_name] # Remove target name from potential outputs
    
    # Calculate targets 
    encodings = [jf.match_rating_codex(n) for n in unique_names]
    target = jf.match_rating_codex(match_name)
    distance = [jf.jaro_winkler_similarity(target, e) for e in encodings]
    
    df = pd.DataFrame(data = [unique_names, encodings, distance]).T
    df.columns = ["name", "encoding", "match_score"]
    df["weight"] = (df["match_score"]*2)**10 # Heavily weigh higher scores
    
    # Sample n names to output, weighted by match_score
    sampled = df.sample(n = limit, weights = "weight")
    sampled = sampled.sort_values(by = "match_score", ascending = False)
    return(sampled["name"].to_list())