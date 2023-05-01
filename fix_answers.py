import sys
import openai
openai.api_key = "YOUR_API_KEY"

def prompt(linePrompt):
    response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=linePrompt,
                # temperature=0.9,
                max_tokens=200,
                # top_p=1,
                # frequency_penalty=0,
                # presence_penalty=0.6,
                # stop=["\n"]
            )
           
            # Print the response
    return response.choices[0].text

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def correctQuestion():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        with open(sys.argv[2], 'a', encoding='utf-8') as f2:
            for line in f:
                # iterate over each word in line
                line = line.strip()
                words = line.split(" ")
                num = words[0]
                f2.write(num + " ")
                for words in chunks(words[1:], 10):
                    linePrompt = "prosím oprav všechny gramatické chyby v této větě. odpovídej v cestině:\n" + " ".join(words) + "\n"
                    text = prompt(linePrompt)          
                    print("Q", " ".join(words))
                    print("A", text)
                    f2.write(text)
                f2.write("\n")


if __name__ == '__main__':
    # print engine list:
    # print(openai.Engine.list())
    correctQuestion()