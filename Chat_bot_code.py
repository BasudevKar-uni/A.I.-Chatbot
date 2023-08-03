"""                                            
 /      \           /  |                          /  |       /      \                                       
/$$$$$$  |  _______ $$ |____    ______    ______  $$ |      /$$$$$$  | __    __   ______    ______   __    __ 
$$ \__$$/  /       |$$      \  /      \  /      \ $$ |      $$ |  $$ |/  |  /  | /      \  /      \ /  |  /  |
$$      \ /$$$$$$$/ $$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |      $$ |  $$ |$$ |  $$ |/$$$$$$  |/$$$$$$  |$$ |  $$ |
 $$$$$$  |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |_ $$ |$$ |  $$ |$$    $$ |$$ |  $$/ $$ |  $$ |
/  \__$$ |$$ \_____ $$ |  $$ |$$ \__$$ |$$ \__$$ |$$ |      $$ / \$$ |$$ \__$$ |$$$$$$$$/ $$ |      $$ \__$$ |
$$    $$/ $$       |$$ |  $$ |$$    $$/ $$    $$/ $$ |      $$ $$ $$< $$    $$/ $$       |$$ |      $$    $$ |
 $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$/   $$$$$$/  $$/        $$$$$$  | $$$$$$/   $$$$$$$/ $$/        $$$$$$$ |
                                                                 $$$/                               /  \__$$ |
                                                                                                    $$    $$/ 
                                                                                                     $$$$$$/     
 /      \ /  |                  /  |           /       \             /  |    
/$$$$$$  |$$ |____    ______   _$$ |_          $$$$$$$  |  ______   _$$ |_   
$$ |  $$/ $$      \  /      \ / $$   |  ______ $$ |__$$ | /      \ / $$   |  
$$ |      $$$$$$$  | $$$$$$  |$$$$$$/  /      |$$    $$< /$$$$$$  |$$$$$$/   
$$ |   __ $$ |  $$ | /    $$ |  $$ | __$$$$$$/ $$$$$$$  |$$ |  $$ |  $$ | __ 
$$ \__/  |$$ |  $$ |/$$$$$$$ |  $$ |/  |       $$ |__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |  $$ |$$    $$ |  $$  $$/        $$    $$/ $$    $$/   $$  $$/ 
 $$$$$$/  $$/   $$/  $$$$$$$/    $$$$/         $$$$$$$/   $$$$$$/     $$$$/  """

import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["question"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chatbot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'bye':
            break


        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["question"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I am not able to find answer to your question but I can refer you to the school website 'http://www.agdav.edu.in'? ")

if __name__ == "__main__":
    chatbot()
