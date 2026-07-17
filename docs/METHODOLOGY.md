# Methodology

## Experimental design

The study uses 100 base intents distributed across Technology, Finance, Healthcare, Marketing, and Sports. Every intent is expressed through ten semantically aligned phrasing conditions:

1. Direct Question
2. Conversational
3. Formal/Professional
4. Informal
5. Conditional
6. Highly Specific
7. Ambiguous
8. Comparative
9. Constraint-Based
10. Role-Based/Expert Framing

This yields 1,000 unique prompts. Each prompt was submitted once to ChatGPT, Claude, and Gemini under provider-default temperature settings and a fixed 1,200-output-token ceiling.

## Data quality and realised sample

The expected design contains 3,000 prompt-model observations. The realised dataset contains 2,984 valid observations; 16 ChatGPT responses are absent. A total of 694 observed responses reached the output-token ceiling. Capped responses remain part of the primary analysis because they represent behaviour under the stated collection protocol. Uncapped and common-prompt analyses assess sensitivity to this choice.

## Derived measures

- **Latent-semantic divergence:** cosine distance from the within-model, within-intent centroid using TF-IDF word/bigram features reduced with Truncated SVD.
- **Lexical instability:** mean pairwise Jaccard distance between content-word sets within a model-intent block.
- **Length deviation:** absolute deviation from the within-block median word count, divided by that median.
- **Structural deviation:** mismatch from the modal response-structure signature within a block.
- **Recommendation-instability proxy:** mean Jaccard distance between heuristically extracted list-item labels, reported only where extraction coverage is adequate.
- **Claim-verification risk proxy:** a transparent rule-based score for unsourced numeric or entity-dense claims. It is not a factuality judgement.
- **Core behavioural sensitivity:** a scaled composite of semantic (0.45), lexical (0.25), length (0.15), and structural (0.15) components.

## Statistical analysis

Base intents are the paired blocks. Friedman tests assess whether outcomes differ across the ten phrasing conditions within each model. Significant omnibus tests are followed by paired Wilcoxon signed-rank comparisons with Holm family-wise error correction. Rank-biserial correlations and Kendall's W quantify effect size.

RQ3 aggregates response-level measures within each model-intent block, then compares the three models with paired Friedman and Wilcoxon-Holm tests across 100 base intents.

## Robustness and validation

The analysis includes:

- full observed data;
- uncapped-only group summaries;
- the 320 prompt IDs observed and uncapped for all three models;
- semantic-heavy, equal-weight, and no-length variants of the composite score;
- a stratified manual-validation sample and coding protocol for the claim-risk proxy.

## Interpretation boundaries

The design contains one observed response per prompt-model pair, not repeated stochastic trials. Findings therefore describe the selected model versions and collection conditions. They do not establish universal or causal effects of wording. Token censoring differs sharply by model and must be considered when interpreting model comparisons. Proxy measures should not be described as verified hallucinations or perfect recommendation extraction.
