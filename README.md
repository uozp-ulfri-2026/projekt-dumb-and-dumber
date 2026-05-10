# projekt-dumb-and-dumber

## Semantic Search

Run the pipeline in this order:

```powershell
python src/extractData.py
python src/embedArticles.py
python src/faissSearch.py --query "Janja Garnbret" --top-k 10
```

## UMAP Visualization

Create an interactive 2D Plotly view for a random sample of 5000 articles:

```powershell
python src/visualizeUmap.py
```

The script caches the 2D UMAP projection in `data/mmc_embeddings/umap_cache/` so reruns reuse the previous layout unless the inputs or settings change. The generated figure shows two side-by-side panels: one colored by clustering and one colored by article topic.

Serve the visualization with FAISS top-1 search enabled:

```powershell
python src/serveUmapSearch.py
```

Then open `http://127.0.0.1:8000/`. Search highlights the top result when that article is part of the sampled UMAP points; otherwise it shows the matched article title and link.
By default the server uses the locally cached sentence-transformers model; add `--allow-model-download` if you need it to download missing model files.
