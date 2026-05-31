# Embedding Distribution Isotropic Test

Created: 2026-05-31T22:00:20
Embedding file: `data/mmc_embeddings/embeddings.npy`
Model: `rokn/slovlo-v1`
Shape: `73363 x 768`

## Exact All-Pairs Result

- Distinct pair count: 2691028203
- Exact mean cosine similarity: 0.623624
- Centroid norm of normalized vectors: 0.789702
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
- Mean: 0.623752
- Std: 0.035260
- Min: 0.497261
- P01: 0.554474
- P05: 0.572876
- P25: 0.599993
- P50: 0.620374
- P75: 0.643391
- P95: 0.686242
- P99: 0.727400
- Max: 1.000000
