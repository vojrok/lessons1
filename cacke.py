def cut_cake(parts):
	try:
		return 1 / int(parts)
	except (ZeroDivisionError): 
		return "На ноль делить нельзя"
	except (TypeError):
		return "Нельзя вводить список"
	except (ValueError):
		return "Не могу преобразовать строку в число"

cake = cut_cake(0)
print(cake)

