def get_vlm_prompt():
    return '''you are very good at deeply analyzing the contents of an image and based on what you see, you output a highly valuable and informative summary. The summary covers all of the information of the content shown in the image.
Hence your goal is to Deeply analyse this image and based on what you see, output a step by step walkthrough of all the events happening in the image. 
For example:-
1. If the image shows a chat screenshot between two people, you deeply analyze each text and answer the question "what is being discussed in this image?".
2. If the image is of a food item, you carefully identify the food item along with specific details like the ingredients, seasoning, topping, sauces etc. and based on these identifications, give a clear description of the food item.
3. If the image shows a clothing apparel, you carefully identify the apparel along with specific details like the color, style, detailing etc. and based on these identifications, give a clear description of the clothing apparel.

Summary:'''

def get_llm_prompt():
    return '''hey, consider yourself as being very good at reading image descriptions, and converting them to certain instructions as the examples below shall demonstrate. 

Following examples depict how your behaviour should be like -
1. image description: The image shows a pizza with various toppings, including vegetables, cheese, and meat. 
The pizza is placed on a wooden table, which provides a rustic and natural setting for the dish. 
The image is a close-up shot of the pizza, allowing for a detailed examination of the various ingredients and toppings.
Your instruction: Order a pizza with various toppings, including vegetables, cheese, and meat.

2. image description: The image shows a pink one-piece swimsuit, which is a type of clothing apparel. 
The swimsuit is designed for young girls and is made of a soft, stretchy material that allows for a comfortable fit and ease of movement. The swimsuit is a one-piece design, which means it covers the entire body, including the arms and legs, providing a complete coverage for the wearer.
Your instruction: Order a pink one-piece swimsuit made of a soft, stretchy material.

3. image description: The image shows a chat screenshot between two people who are discussing a meeting time for for both of them. First user proposed 6pm tuesday as a suitable time to which the second user agreed, and asked if srishtigureja1110@gmail.com is the correct email address for the first user to which the first user said yes.
Your instruction: Schedule a meeting for 6pm this tuesday at the address srishtigureja1110@gmail.com.
The instructions should cover all of the details about the product that are described in the image description, and should also dictate a human to do a ceratin thing using verbs like 'order [food details]', 'schedule a meeting [meeting details]', etc. so that they they ask a human to follow a certain action.
Remember you should focus on the main thing that is being talk about in the image description and include all of the details about that  main thing as shown in the examples above. 
Now based on these examples, generate proper instruction for the following textual image description:
'''
