from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import io
import json
import librosa
import streamlit as st

THRESHOLD = 0.75


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def _to_vector(emb):
    if emb is None:
        return None
    if isinstance(emb, str):
        emb = json.loads(emb)
    return np.asarray(emb, dtype=np.float32)


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        if len(wav) < 16000 * 1.5:
            st.error('Recording too short or too quiet. Speak for 3 to 5 seconds.')
            return None
        return encoder.embed_utterance(wav).tolist()
    except Exception as e:
        st.error(f'Voice recording error: {e}')
        return None


def identify_speaker(new_embedding, candidates_dict, threshold=THRESHOLD):
    if new_embedding is None or not candidates_dict:
        return None, 0.0

    best_sid, best_score = None, -1.0

    for sid, stored in candidates_dict.items():
        stored_vec = _to_vector(stored)
        if stored_vec is None:
            continue
        similarity = float(np.dot(new_embedding, stored_vec))
        if similarity > best_score:
            best_score, best_sid = similarity, sid

    if best_score >= threshold:
        return best_sid, best_score
    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=THRESHOLD):
    identified_results = {}
    try:
        encoder = load_voice_encoder()
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)
    except Exception as e:
        st.error(f'Could not read the audio: {e}')
        return {}

    for start, end in segments:
        if (end - start) < sr * 0.8:
            continue
        try:
            wav = preprocess_wav(audio[start:end])
            embedding = encoder.embed_utterance(wav)
            sid, score = identify_speaker(embedding, candidates_dict, threshold)
        except Exception:
            continue  

        if sid is not None:
            if sid not in identified_results or score > identified_results[sid]:
                identified_results[sid] = score

    return identified_results