# Embedding Distribution Isotropic Test

Created: 2026-05-31T21:44:04
Embedding file: `data/mmc_embeddings/embeddings.npy`
Model: `intfloat/multilingual-e5-large`
Shape: `73363 x 1024`

## Exact All-Pairs Result

- Distinct pair count: 2691028203
- Exact mean cosine similarity: 0.795936
- Centroid norm of normalized vectors: 0.892154
- Interpretation: `strongly_anisotropic`

The exact mean is computed without materializing all pairs, using the identity based on the norm of the sum of normalized vectors.

## Embedding Norms

- Min: 1.000000
- Mean: 1.000000
- Max: 1.000000
- Std: 0.000000
- Zero vectors: 0

## Random Pair Sample

- Sample count: 200000
- Mean: 0.795953
- Std: 0.019733
- Min: 0.710700
- P01: 0.752811
- P05: 0.764982
- P25: 0.782611
- P50: 0.795186
- P75: 0.808486
- P95: 0.829173
- P99: 0.846421
- Max: 1.000000
