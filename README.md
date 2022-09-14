# Target-Guided Open-Domain Conversation Planning

This repository contains the code to construct the test set we developed in:

Yosuke Kishinami, Reina Akama, Shiki Sato, Ryoko Tokuhisa, Jun Suzuki and Kentaro Inui. Target-Guided Open-Domain Conversation Planning.

## Requirements
nltk==3.4


## Test set construction
1. Download `start_corpus.pkl` and `target_set.pkl` from [the ConvAI2 dataset](https://www.dropbox.com/s/1fw2gwpuyud2bkq/convai2.zip?dl=0) published on https://github.com/zhongpeixiang/CKC

2. Run the following command
```
python construct_tgcp_dataset.py --start_utter data/convai2/start_corpus.pkl --target_word data/convai2/target_set.pkl --id id.txt --output {output file}
```

## Evaluation of a generated conversation plan
You can evaluate the conversation plan in the TGCP task by run the following command:
```
python evaluate.py --input data/result.jsonl
```

Note: `result.jsonl` should be in the following jsonl format.

`conversation_plan` should separate utterances with `[SEP]`.
```
{"target_word": "book", "conversation_plan": "Hi, What do you do for living?[SEP]I work as an engineer.[SEP]That sounds nice. How do you learn coding?[SEP]I read and learn from technical books."}
{"target_word": "dog", "conversation_plan": "..."}
...
```


## Citation
If you use this If you use anything in this repository, please cite:

Yosuke Kishinami, Reina Akama, Shiki Sato, Ryoko Tokuhisa, Jun Suzuki and Kentaro Inui.
**Target-Guided Open-Domain Conversation Planning**.
*Proceedings of the 29th International Conference on Computational Linguistics*,
Oct. 2022.

```
@InProceedings{kishinami2022tgcp,
  title={Target-Guided Open-Domain Conversation Planning}
  author={Yosuke Kishinami and Reina Akama and Shiki Sato and Ryoko Tokuhisa and Jun Suzuki and Kentaro Inui}
  booktitle={Proceedings of the 29th International Conference on Computational Linguistics}
  year={2022}
}
```
