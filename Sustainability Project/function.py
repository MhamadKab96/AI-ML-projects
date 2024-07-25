import anthropic

class myClass:
    
    @staticmethod
    def enter_prompt(prompt) -> str:
      client = anthropic.Client(api_key= "INSERT-API-KEY")
      
      response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens = 1024,
        messages=[
            {"role": "user", "content": prompt} 
        ]
                                        )
      readable_text = response.content[0].text
      return readable_text
