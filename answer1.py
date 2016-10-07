dialog = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
def get_answer(question, answer):
	return answers.get(question)

print(get_answer('пока', dialog))