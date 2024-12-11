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

print("플레이어: 올해로 모솔 인생 어언 25년 째...")
print("그런 나에게 친구녀석이 추천해준 연애 훈련 캠프.")
print("처음엔 반신반의했지만, 2주간 어찌저찌 수업을 듣다보니 이제 수료를 앞둔 마지막 단계까지 왔다.")
print("들어보니 이 프리미엄 과정만의 특별 파이널테스트가 있다던데...\n")

print("안내자: 올해는 나도 솔로 탈출!")
print("특별 맞춤 연애 코칭 프리미엄 과정의 모든 수업을 들으시다니... 수고가 많으셨습니다.")
print("이제 코스 수료까지 마지막 한 걸음! 수료를 위한 마지막 조건은 바로...")
print("!!~~AI 그녀의 마음을 읽어라~~!!")
print("당신이 해야 할 일은 단 하나!")
print("바로 AI, 키타부키 후가미 씨의 마음을 읽어 그녀와 하루동안 성공적인 데이트를 즐기는 것입니다.")
print("그녀와의 데이트에서 성공적인 결과를 만들어낸다면, 당신은 프리미엄 과정을 훌륭하게 끝마칠 수 있을겁니다.")
print("\n플레이어: 뭐? 갑자기 시뮬레이션 게임이라니... 그것도 AI와 함께라니 썩 내키진 않지만, 마지막까지 온 김에 그냥 막판에 망치고 싶은 생각은 없다.")
print("AI라지만 감정이 느껴진다고 하니... 과연 내가 잘 할 수 있을까?\n")

total_score = 0

print("연애 시뮬레이션 게임에 오신 것을 환영합니다!")
print("오늘 하루의 데이트는 총 5라운드로 진행됩니다.")
print("그녀가 하는 말을 잘 듣고, 그녀는 어떤 감정으로 그 말을 했을지! 잘 알아 맞춰보세요!")
print("모든 라운드가 끝난 후, 총점이 공개됩니다")
print("문장에 대한 감정을 추측해 입력하세요: 매우 긍정적, 긍정적, 보통, 부정적, 매우 부정적")


for round_num in range(1, 6):  
    sentence = random.choice(round_sentences[round_num]) 
    
    print(f"\nRound {round_num}")

    if round_num == 0:
        print("첫 만남: 당신은 그녀와 처음으로 만났습니다. 설렘과 긴장이 교차하는 순간입니다.")
    elif round_num == 1:
        print("카페에서의 대화: 서로에 대해 알아가기 위해 카페에서 이야기를 나눕니다.")
    elif round_num == 2:
        print("갈등의 순간: 대화 중 약간의 오해와 갈등이 발생했습니다. 상황을 잘 해결해야 합니다.")
    elif round_num == 3:
        print("관계의 진전: 갈등을 극복하고 서로 더 가까워지는 시간을 가집니다.")
    elif round_num ==4:
        print("마지막 결정: 데이트의 끝, 서로의 진심을 확인하는 중요한 순간입니다.")

        
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
    print("이것으로 당신은 특별 맞춤 연애 코칭 프리미엄 과정을 훌륭하게 끝마쳤습니다.")
    print("수료증을 드립니다!")
else:
    print("이런, 연애에 실패했습니다.")
    print("아쉽지만 당신은 특별 맞춤 연애 코칭 프리미엄 과정을 수료하지 못했습니다...")
    print("그런 당신을 위해 3회 추가 수업 50% 할인권을 드립니다!")
    print("그녀의 마음을 얻기 위해 다시 한 번 도전해보세요!")
