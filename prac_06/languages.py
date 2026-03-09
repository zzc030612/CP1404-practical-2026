from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    languages = [ruby, python, visual_basic]
    languages_dynamic = []
    for language in languages:
        dynamic = language.is_dynamic()
        if dynamic:
            languages_dynamic.append(language.name)
    print("Dynamically typed languages are: ")
    for i in languages_dynamic:
        print(i)


main()