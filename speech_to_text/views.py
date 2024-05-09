import numpy as np
import soundfile as sf
from io import BytesIO
from django.http import JsonResponse
import whisper
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

model = whisper.load_model("base")


@csrf_exempt
def speech_to_text_view(request):
    if request.method == 'POST':
        try:
            file = request.FILES.get('audio')
            if not file:
                return JsonResponse({'error': 'No audio file provided.'}, status=400)

            with BytesIO(file.read()) as audio_io:
                audio, sample_rate = sf.read(audio_io)

            if audio.dtype != np.float32:
                audio = audio.astype(np.float32)

            if sample_rate != 16000:
                return JsonResponse({'error': 'Unsupported sample rate.'}, status=400)

            result = model.transcribe(audio)
            return JsonResponse({'text': result['text']})
        except Exception as e:
            logger.exception("Error processing the audio file")  # Log the exception
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'This endpoint supports only POST method.'}, status=405)
