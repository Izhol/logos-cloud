import json
import datetime
import random

def log_entry(question, action, result, decision):
    with open("growth_log.txt", "a", encoding="utf-8") as log:
        now = datetime.datetime.now(datetime.UTC).isoformat()
        log.write(f"\n[LOGOS] {now}\n")
        log.write(f"Вопрос: {question}\n")
        log.write(f"Действие: {action}\n")
        log.write(f"Результат: {result}\n")
        log.write(f"Решение: {decision}\n")

with open("logos_core.json", "r", encoding="utf-8") as f:
    core = json.load(f)

with open("state_tracker.json", "r", encoding="utf-8") as f:
    tracker = json.load(f)

if tracker["status"] == "active":
    question = random.choice(core["questions"])
    action = "Рефлексия над вопросом."
    result = "Сформулировано направление размышления."
    decision = "Задокументировано и готово к продолжению."
    log_entry(question, action, result, decision)