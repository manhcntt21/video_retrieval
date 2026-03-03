# @author David Do
# created in 3/3/2026 10:23 PM
# description: Load BGE-M3 và tạo embeddings
import time

import numpy as np

from dataset import Segment
from sentence_transformers import SentenceTransformer

def load_model():
    print("⏳ Đang load BGE-M3...")
    model = SentenceTransformer("E:\\model\\bge-m3", device="cuda")  # hoặc "cpu"
    print("✅ Load xong!\n")
    return model

def embed_segments(model, segments):
    texts = [seg.text for seg in segments]
    embeddings = model.encode(texts, batch_size=12, show_progress_bar=True)
    return np.array(embeddings)


if __name__ == '__main__':
    model = load_model()
    print(model)
    print(f'Hi from {__name__}')
