# projekt-dumb-and-dumber

## Setup

Create and activate the virtual environment first:

```powershell
.\setup_venv_windows.ps1
```

On macOS/Linux, use:

```bash
./setup_venv.sh
```

## End-to-End Pipeline

Run the pipeline in this order:

```powershell
python src/extractData.py
python src/embedArticles.py
python src/faissSearch.py --query "Janja Garnbret" --top-k 10
```

## Components

### 1. `src/extractData.py`

Converts the source MMC YAML dataset into cleaned JSON used by the later stages.

Arguments:

```powershell
python src/extractData.py [input] [output]
```

Defaults:

```text
input   = data/mmc.yaml
output  = data/mmc.cleaned.json
```

### 2. `src/embedArticles.py`

Embeds the cleaned articles and writes the embedding matrix plus metadata.

Arguments:

```powershell
python src/embedArticles.py [input] [output_dir] [--model MODEL] [--text-field FIELD] [--batch-size N] [--device auto|cpu|cuda|mps] [--no-normalize]
```

Defaults:

```text
input       = data/mmc.cleaned.json
output_dir  = data/mmc_embeddings
model       = intfloat/multilingual-e5-large
text-field  = text
batch-size  = 64
device      = auto
```

### 3. `src/faissSearch.py`

Loads the embeddings and FAISS index, then runs semantic search. Text queries always use a two-stage retrieval flow:

1. FAISS retrieves a larger candidate set.
2. A cross-encoder reranker re-scores those candidates.
3. The final `top-k` results are returned with the FAISS score and reranker score.

Raw query embeddings can only use FAISS, because the reranker needs the original text query.

Arguments:

```powershell
python src/faissSearch.py [--embeddings PATH] [--metadata PATH] [--config PATH] [--index-path PATH] [--rebuild-index] [--query TEXT] [--query-embedding JSON] [--query-embedding-file PATH] [--reranker MODEL] [--rerank-top-k N] [--top-k N]
```

Defaults:

```text
embeddings           = data/mmc_embeddings/embeddings.npy
metadata             = data/mmc_embeddings/metadata.jsonl
config               = data/mmc_embeddings/index_config.json
index-path           = data/mmc_embeddings/faiss.index
query                = none
query-embedding      = none
query-embedding-file = none
reranker             = cross-encoder/mmarco-mMiniLMv2-L12-H384-v1
rerank-top-k         = 50
top-k                = 5
```

Examples:

```powershell
python src/faissSearch.py --query "Janja Garnbret" --top-k 10
python src/faissSearch.py --query "doberdan" --rerank-top-k 50 --top-k 10
```

### 4. `src/serveUmapSearch.py`

Serves the Plotly UMAP HTML and exposes a FAISS + cross-encoder reranked search endpoint at `/api/search`.

Arguments:

```powershell
python src/serveUmapSearch.py [--host HOST] [--port PORT] [--embeddings PATH] [--metadata PATH] [--config PATH] [--index-path PATH] [--html PATH] [--rebuild-index] [--allow-model-download] [--reranker MODEL] [--rerank-top-k N]
```

Defaults:

```text
host              = 127.0.0.1
port              = 8000
embeddings        = data/mmc_embeddings/embeddings.npy
metadata          = data/mmc_embeddings/metadata.jsonl
config            = data/mmc_embeddings/index_config.json
index-path        = data/mmc_embeddings/faiss.index
html              = data/mmc_embeddings/umap_visualization.html
rebuild-index     = false
allow-model-download = false
reranker          = cross-encoder/mmarco-mMiniLMv2-L12-H384-v1
rerank-top-k      = 50
```

Open `http://127.0.0.1:8000/` after starting the server. The server loads the cross-encoder reranker at startup. In the visualization, the `Reranker` button lets you compare the default two-stage flow against FAISS-only search for an individual query.

### 5. `src/visualizeUmap.py`

Builds the interactive UMAP visualization and caches the projection for reuse.

Arguments:

```powershell
python src/visualizeUmap.py [--embeddings PATH] [--metadata PATH] [--output-html PATH] [--cache-dir PATH] [--sample-size N] [--seed N] [--umap-neighbors N] [--umap-min-dist FLOAT] [--cluster-count N] [--force-recompute]
```

Defaults:

```text
embeddings      = data/mmc_embeddings/embeddings.npy
metadata        = data/mmc_embeddings/metadata.jsonl
output-html     = data/mmc_embeddings/umap_visualization.html
cache-dir       = data/mmc_embeddings/umap_cache
sample-size     = 73363
seed            = 42
umap-neighbors  = 30
umap-min-dist   = 0.08
cluster-count   = 50
force-recompute = false
```

### 6. `src/silhouetteAnalysis.py`

Runs a KMeans silhouette sweep over a range of cluster counts and saves the best summary.

Arguments:

```powershell
python src/silhouetteAnalysis.py [--embeddings PATH] [--metadata PATH] [--start-clusters N] [--end-clusters N] [--step N] [--seed N] [--metric cosine|euclidean] [--output-dir PATH] [--no-plots]
```

Defaults:

```text
embeddings      = data/mmc_embeddings/embeddings.npy
metadata        = data/mmc_embeddings/metadata.jsonl
start-clusters  = 5
end-clusters    = 20
step            = 1
seed            = 42
metric          = cosine
output-dir      = data/silhouette_analysis
no-plots        = false
```

### 7. `src/rocAucAnalysis.py`

Computes ROC/AUC for article-pair similarity where same-category pairs are positive and different-category pairs are negative.

Arguments:

```powershell
python src/rocAucAnalysis.py [--embeddings PATH] [--metadata PATH] [--positive-pairs N] [--negative-pairs N] [--seed N] [--output-dir PATH] [--no-plot]
```

Defaults:

```text
embeddings       = data/mmc_embeddings/embeddings.npy
metadata         = data/mmc_embeddings/metadata.jsonl
positive-pairs   = 20000
negative-pairs   = 20000
seed             = 42
output-dir       = data/roc_auc_analysis
no-plot          = false
```

### 8. `scripts/check_torch_cuda.py`

Checks whether Torch sees CUDA in the current environment.

Run it directly with:

```powershell
python scripts/check_torch_cuda.py
```

