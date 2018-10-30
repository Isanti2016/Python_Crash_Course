class AnonymousSurvey():
    """收集问题的答案"""
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        """显示问卷"""
        print(self.question)
    
    def store_response(self, new_response):
        """存储回答"""
        self.responses.append(new_response)
        
    def show_results(self):
        """显示回答"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
