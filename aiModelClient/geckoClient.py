import vertexai
from vertexai.language_models import CodeGenerationModel
from google.oauth2 import service_account
import os

class GeckoClient:
    def __init__(self):
        # Load the credentials from the service account file
        file_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        credentials = service_account.Credentials.from_service_account_file(file_path)

        vertexai.init(project="gen-lang-client-0962130176",
                      location="us-central1", credentials=credentials)
        self.model = CodeGenerationModel.from_pretrained("code-gecko@latest")

    async def prompt(self, prefix, suffix):
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 64,
            "temperature": 0.9
        }
        response = await self.model.predict_async(prefix, suffix = suffix, **parameters)
        return response
