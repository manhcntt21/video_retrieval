# @author David Do
# created in 3/3/2026 10:26 PM
# description:
import numpy as np

from dataset import Segment


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Tính cosine similarity giữa 1 vector và ma trận vectors."""
    a_norm = a / (np.linalg.norm(a) + 1e-10)
    b_norm = b / (np.linalg.norm(b, axis=1, keepdims=True) + 1e-10)
    return b_norm @ a_norm


def search(
        query: str,
        model,
        segments: list[Segment],
        embeddings: np.ndarray,
        top_k: int = 3,
        threshold: float = 0.3,
) -> list[dict]:
    """
    Tìm kiếm semantic trong transcript.

    Args:
        query: Câu hỏi tự nhiên của người dùng
        top_k: Số kết quả trả về
        threshold: Ngưỡng similarity tối thiểu (0-1)
    """
    # Embed query
    q_vec = model.encode([query])[0]

    # Tính similarity với tất cả segment
    scores = cosine_similarity(q_vec, embeddings)

    # Lấy top-k kết quả trên threshold
    ranked_idx = np.argsort(scores)[::-1]
    results = []
    for idx in ranked_idx[:top_k]:
        score = float(scores[idx])
        if score < threshold:
            break
        seg = segments[idx]
        results.append({
            "score": score,
            "segment": seg,
            "timestamp": f"{int(seg.start // 60):02d}:{int(seg.start % 60):02d} → {int(seg.end // 60):02d}:{int(seg.end % 60):02d}",
        })

    return results


if __name__ == '__main__':
    print(f'Hi from {__name__}')
