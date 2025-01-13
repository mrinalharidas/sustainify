import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyA5CE1G5QOM5NuWbum8ZTJ8FudHYeIEuYk")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "product type or genre recognition from a given title from a shopping website \nonly want a single word or at max two word answer",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. Here are some examples of how I would respond:\n\n**Input:** \"Samsung 65-Inch Class Crystal UHD 4K Smart TV\"\n**Output:** TV\n\n**Input:** \"Levi's Men's 501 Original Fit Jeans\"\n**Output:** Jeans\n\n**Input:** \"Instant Pot Duo 7-in-1 Electric Pressure Cooker\"\n**Output:** Cooker\n\n**Input:** \"Apple MacBook Pro 13-inch\"\n**Output:** Laptop\n\n**Input:** \"The Very Hungry Caterpillar Board Book\"\n**Output:** Book\n\n**Input:** \"Nike Air Zoom Running Shoes\"\n**Output:** Shoes\n\n**Input:** \"KitchenAid Stand Mixer\"\n**Output:** Mixer\n\n**Input:** \"Nintendo Switch Console\"\n**Output:** Console\n\n**Input:** \"Lego Classic Creative Brick Box\"\n**Output:** Lego\n\n**Input:** \"Ray-Ban Aviator Sunglasses\"\n**Output:** Sunglasses\n",
      ],
    },
  ]
)

response = chat_session.send_message("SARAL HOME EASY LIVING Soft Microfiber Anti Slip Bathmat Set of 2 (Grey, 35X50 Cm), Large Rectangle")

print(response.text)