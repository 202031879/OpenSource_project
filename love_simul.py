import random
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

round_sentences = {
    1: [
        "It's so exciting to finally meet you!",  # 매우 긍정적
        "I'm a little nervous to meet someone new.",  # 긍정적
        "I hope this goes well."  # 보통
    ],
    2: [
        "This place is nicer than I expected.",  # 긍정적
        "The food here is fine, I guess.",  # 보통
        "The service is not as good as I thought it would be."  # 부정적
    ],
    3: [
        "I feel like you're not really listening to me.",  # 부정적
        "Sometimes I just need you to understand me better.",  # 보통
        "I appreciate your effort to make things right."  # 긍정적
    ],
    4: [
        "I think we're really starting to understand each other.",  # 긍정적
        "I enjoy spending time with you.",  # 보통
        "It's nice to see you putting in the effort."  # 긍정적
    ],
    5: [
        "I'm not sure what the future holds, but I feel hopeful.",  # 보통
        "I think you're really special.",  # 긍정적
        "I need to think about how I truly feel."  # 부정적
    ]
}

emotion_levels = ["매우 부정적", "부정적", "보통", "긍정적", "매우 긍정적"]

def calculate_score(ai_emotion, user_input):
    
    if user_input not in emotion_levels:
        return 0, ai_emotion 

    ai_index = emotion_levels.index(ai_emotion)
    user_index = emotion_levels.index(user_input)
    difference = abs(ai_index - user_index)

    if difference == 0: 
        return 100, ai_emotion
    elif difference == 1:  
        return 50, ai_emotion
    else:  
        return 0, ai_emotion


total_score = 0

print("연애 시뮬레이션 게임에 오신 것을 환영합니다!")
print("문장에 대한 감정을 추측해 입력하세요: 매우 긍정적, 긍정적, 보통, 부정적, 매우 부정적")


for round_num in range(1, 6):  
    sentence = random.choice(round_sentences[round_num]) 
    
    print(f"\nRound {round_num}")
    print(f"문장: {sentence}")
    
    user_input = input("이 문장의 감정 상태를 입력하세요: ").strip()
    
   
    result = sentiment_analyzer(sentence)[0]
    ai_score = result["score"] if result["label"] == "POSITIVE" else 1 - result["score"]
    
   
    if ai_score > 0.9:
        ai_emotion = "매우 긍정적"
    elif ai_score > 0.7:
        ai_emotion = "긍정적"
    elif ai_score > 0.5:
        ai_emotion = "보통"
    elif ai_score > 0.3:
        ai_emotion = "부정적"
    else:
        ai_emotion = "매우 부정적"
    
   
    round_score, ai_emotion = calculate_score(ai_emotion, user_input)
    total_score += round_score

    print(f"AI 감정 분석 결과: {ai_emotion} (확률: {ai_score*100:.2f}%)")
    print(f"라운드 점수: {round_score}점")
    print(f"현재 총점: {total_score}점")


print("\n게임 종료!")
if total_score >= 400:
    print("축하합니다! 연애에 성공했습니다.")
else:
    print("아쉽습니다. 연애에 실패했습니다.")
