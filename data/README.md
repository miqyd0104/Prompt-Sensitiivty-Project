# Data layers

The dataset is organised by pipeline stage so that provenance is visible without opening a notebook.

| Layer | File | Description |
|---|---|---|
| Collection | `collection/pre_data_collection.xlsx` | Experimental prompt design: 100 base intents × 10 phrasing variants across five domains |
| Raw | `raw/data_collection_all_responses.xlsx` | Provider responses and collection metadata written by Notebook 01 |
| Processed | `processed/analysis_ready_responses.csv` | Tidy, validated input used by Notebook 03 |

The processed file contains 2,984 observed responses from an expected design of 3,000. Sixteen ChatGPT responses were not collected. Responses that reached the fixed 1,200-token ceiling are retained and flagged rather than silently removed.

The response text is research data generated under the collection protocol. Model and timestamp fields should be retained when analysing or redistributing derived results so that provenance is not lost.
