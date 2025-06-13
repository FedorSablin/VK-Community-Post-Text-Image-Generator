from openai import OpenAI

class ImageGenerator:
    def __init__(self, openai_key):
        self.client = OpenAI(api_key=openai_key)

    def generate_image(self, prompt):
        try:
            response = self.client.images.generate(
              model="dall-e-3",
              prompt=prompt,
              size="1024x1024",
              quality="standard",
              n=1,
            )

            image_url = response.data[0].url
            return image_url
        except Exception as e:
            raise Exception(f"Ошибка при генерации изображения: {str(e)}")
