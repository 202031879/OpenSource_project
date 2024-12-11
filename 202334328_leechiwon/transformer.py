from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 문장들 (예시: "텍스트 1", "텍스트 2")
texts = [
    "오늘 날씨가 좋네요! 바람도 불고 해가 쨍쨍해요.",
    "새로운 영화가 나왔는데 정말 재미있어요. 꼭 보세요!",
    "정말 화나서 어떻게 해야 할지 모르겠어요...",
    "친구들과 즐거운 시간을 보냈어요. 최고였어요!"
]

# 카테고리: 예시 (긍정, 부정, 중립)
labels = ["긍정", "긍정", "부정", "긍정"]

# 문장 임베딩을 위한 모델 로드
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# 토큰화
batch_size = 4  # 조정 가능한 배치 크기
for i in range(0, len(texts), batch_size):
    batch_texts = texts[i:i + batch_size]
    encoded_input = tokenizer(batch_texts, padding=True, truncation=True, return_tensors='pt', max_length=512)

    # 모델 추론
    with torch.no_grad():
        outputs = model(**encoded_input)

    # 예측된 라벨
    predicted_labels = torch.argmax(outputs.logits, dim=1)

    # 결과 출력
    for text, label in zip(batch_texts, predicted_labels):
        print(f"Text: {text}")
        print(f"Predicted Label: {model.config.id2label[label.item()]}")
        print(f"True Label: {labels[texts.index(text)]}")  # 실제 라벨
        print("-" * 30)