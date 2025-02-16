class Novel:
    def __init__(self, title):
        self.title = title
        self.chapters = {}

    def write_novel_to_bd(self, chapters):
        self.chapters = chapters
        with open(f"{self.titles}.join", 'w', encoding='UTF-8') as json_file:
            loaded_data = json.dump(self.chapters, json_file,
                                    ensure_ascii=False)
        logger.info(f"Главы в новелле записаны в файл {self.title}.json")
        