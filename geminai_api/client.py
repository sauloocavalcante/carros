import google.generativeai as genai
import os

google_api_key = os.getenv('GOOGLE_API_KEY')

def get_car_ai_bio(model, brand, year):
    prompt = """
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale características desse modelo.
    """
    genai.configure(api_key=google_api_key)
    prompt = prompt.format(brand, model, year)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text