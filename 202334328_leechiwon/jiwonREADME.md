# SNS Content classification

## Introduce project
this project classify SNS content (text) into predefined categories (e.g., positive, negative, neutral) using Huggingface's transformers library.

## Example
![Example](https://github.com/zeewon0123/github_test/blob/main/%ED%85%80%ED%94%84.png)

## Requirement
- Python 3.x
- torch
- transformers

## How to use
- 1.**Prepare sentence** (e.g., "오늘 날씨가 좋네요! 바람도 불고 해가 쨍쨍해요.",
    "새로운 영화가 나왔는데 정말 재미있어요. 꼭 보세요!")
- 2.**Define Category**: Label
- 3.**Model & Tokenizer setup**: Load the sentence transformer model and tokenizer from Huggingface.
- 4.**Batch processing**
  
## Reference
This script uses pretrained models from Huggingface, **the model nlptown/bert-base-multilingual-uncased-sentiment** 
**https://neos518.tistory.com/263**