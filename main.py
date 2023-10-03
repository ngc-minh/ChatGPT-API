import openai

openai.api_key = "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"

completion = openai.Completion.create(
  model="text-davinci-003",
  prompt=str(input()),
  temperature=0.9,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

response = completion.choices[0].text
print(response)