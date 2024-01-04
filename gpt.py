from openai import OpenAI
import time

t = 0
userInput = "Therapist: Welcome to our session. How are you feeling today? Patient: I'm okay, thanks. A bit anxious about this, to be honest. Therapist: That's perfectly normal. Let's start by discussing what brings you here. Could you share more about your current challenges? Patient: Sure. For the past few months, I've been under a lot of stress. My job in marketing is really high-pressure, with tight deadlines. I often find myself working late, even on weekends. Therapist: It sounds like your work is demanding a lot of your time and energy. How does this workload affect your daily routine? Patient: Well, I usually wake up already feeling stressed about the day. I check my emails first thing in the morning, and there’s always a crisis at work. It sets a negative tone for my day. Therapist: Starting the day with work stress can be overwhelming. How do you manage this stress throughout the day? Patient: I don’t really. I just push through. Lunch breaks are often skipped, and I drink way too much coffee. By the evening, I'm exhausted but still wired from the caffeine and stress. Therapist: It's important to take breaks for your mental and physical well-being. What happens when you get home from work? Patient: I'm usually too tired to do anything. I know I should cook or exercise, but I end up ordering takeout and watching TV until I go to bed. I feel guilty about not being more productive. Therapist: It's understandable to feel that way, but it's also important to not be too hard on yourself. How about your sleep? How has that been affected? Patient: Falling asleep is tough. My mind races with thoughts about work, deadlines, or things I might have missed. It takes hours to fall asleep, and then I wake up feeling unrested. Therapist: Sleep disruption can significantly impact your well-being. Let's explore strategies to improve your sleep later. For now, can you tell me about your support system? Patient: My partner tries to be supportive, but I don't want to burden them with my work issues. My parents live far away, and my friends are busy with their own lives. I feel quite isolated. Therapist: Sharing your concerns with loved ones can be very therapeutic. Let’s think about ways you can reach out. Now, have you noticed any physical symptoms due to this stress? Patient: Yes, I get headaches often, and my neck is always tense. I know I should see a doctor or get a massage, but I never find the time. Therapist: Physical health is closely tied to mental health. Prioritizing self-care is key. Let's talk about your weekends. How do you spend them? Patient: Mostly catching up on work. I know weekends should be for relaxing, but I can’t help but think about work. Sometimes, I force myself to go out with friends, but even then, my mind is on work. Therapist: It seems like work is dominating your thoughts and life. Let's work on creating boundaries between work and personal time. How do you feel about setting specific 'no work' times during your evenings and weekends? Patient: That sounds good, but it's hard to switch off. The thought of not working makes me anxious. Therapist: It's a common feeling, especially in high-pressure jobs. We can start small, like setting aside an hour each evening where you focus on a relaxing activity. How does that sound? Patient: I can try. Maybe reading or listening to music? Therapist: Yes, those are excellent choices. Reconnecting with hobbies can be a great stress reliever. Now, let’s discuss your diet and exercise. How are those areas? Patient: Not great. My diet is mostly takeout and processed food. I know I should cook more. As for exercise, I just don't have the energy for it. Therapist: Nutrition and physical activity play a significant role in mental health. We can explore simple and manageable changes in these areas. How about starting with one home-cooked meal per week and a short walk every other day? Patient: That seems doable. I used to enjoy cooking. Therapist: Rediscovering old passions can be very fulfilling. Let's also think about mindfulness or meditation. Have you tried any relaxation techniques? Patient: I tried meditation a few times, but my mind wanders, and I get frustrated. Therapist: It's common for beginners to feel that way. Meditation is a skill that develops with practice. We can start with short, guided sessions. How do you feel about that? Patient: I'm willing to give it another try. Therapist: Great. Remember, the goal is not to clear your mind but to become more aware of your thoughts without judgment. Now, let's talk about your long-term goals. What would you like to achieve through therapy? Patient: I want to feel less stressed and more in control of my life. I also want to improve my relationships and have a better work-life balance. Therapist: Those are excellent goals. Therapy is a journey, and we'll work together towards achieving these goals. Do you have any questions or concerns as we wrap up today's session? Patient: No, this has been really helpful. I feel more hopeful. Therapist: I'm glad to hear that. Let’s schedule our next session for the same time next week. In the meantime, try the relaxation exercises and the 'no work' hour in the evening. We'll review how it went in our next session. Patient: Thank you, Dr. Smith. I'll try those out. See you next week. Therapist: You're welcome. Take care, and remember, small steps can lead to big changes. "
prompt = (
    "Instruction: Use first-person narration in the response. Give a response in JSON format. Don't add anything else to the response than the JSON file content."
    + "\n"
    + "Important instructions when writing the note: The whole note file should include no more than 50 words."
    + "\n"
    + " Make sure to add a suitable keyword and format it bold before the phrase. Keyword should be the single word summary of the phrase"
    + "\n"
    + "Use point form which each point is no longer than 12 words."
    + "\n"
    + "The phrases should only include the most important information."
    + "\n"
    + "I’m developing a web app interface which will record the conversation of a psychological therapist and a patient and generate notes from the ongoing conversation. I provide keywords and phrases, so that the therapist can build complete notes using my suggestions. The recorded text will be fed periodically to update the note."
    + "\n"
    + "The note will be written in DEP (data, evaluation and plan) standards. The three topics; Data, Evaluation and Plan must consist of text phrases of a condensed summary of important key points discussed"
    + "\n"    
    + " Generate the note according to the next part of the conversation given below;"
    + userInput
    + "\n"
    + "Exmaple template: {'Data': \n['**Keyword**: Phrase'\n'**Keyword**: Phrase'\n'**Keyword**: Phrase'\n...],  'Evaluation': \n['**Keyword**: Phrase'\n'**Keyword**: Phrase'\n'**Keyword**: Phrase'\n...],  'Plan': \n['**Keyword**: Phrase'\n'**Keyword**: Phrase'\n'**Keyword**: Phrase'\n...]} "   

)


client = OpenAI(
    api_key="",
)
start = time.time()


stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
    temperature=0,
    top_p=0,
)

end = time.time()
t += end - start
stri = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
        stri += chunk.choices[0].delta.content

print()
print(t)