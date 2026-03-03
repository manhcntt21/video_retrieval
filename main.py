# @author David Do
# created in 3/3/2026 10:11 PM
# description:
import time

import numpy as np

from dataset import TRANSCRIPT_DATA
from model import load_model, embed_segments
from search import search

DEMO_QUERIES = [
    "chi phí triển khai machine learning trên cloud",
    "doanh thu quý 3 tăng bao nhiêu phần trăm",
    "vấn đề nhân lực trong lĩnh vực AI",
    "kế hoạch ra mắt sản phẩm mới tháng 11",
    "ứng dụng AI trong bệnh viện và y tế",
    "ngân sách marketing quý 4",
]


def print_results(query: str, results: list[dict]):
    bar = "─" * 60
    print(f"\n{'═' * 60}")
    print(f"🔍 Query: \"{query}\"")
    print(f"{'═' * 60}")

    if not results:
        print("  ⚠️  Không tìm thấy kết quả phù hợp (similarity quá thấp).")
        return

    for i, r in enumerate(results, 1):
        seg = r["segment"]
        score = r["score"]
        bar_len = int(score * 20)
        bar_vis = "█" * bar_len + "░" * (20 - bar_len)

        print(f"\n  #{i}  [{bar_vis}] {score:.3f}")
        print(f"  📹  {seg.video}")
        print(f"  ⏱️   {r['timestamp']}")
        print(f"  💬  {seg.text}")

    print()


if __name__ == "__main__":
    print("=" * 62)
    print("  🎬  Video Semantic Search — BGE-M3 (sentence-transformers)")
    print("=" * 62)
    print(f"  📂 {len(TRANSCRIPT_DATA)} segments | "
          f"{len(set(s.video for s in TRANSCRIPT_DATA))} videos\n")

    # ── Đổi thành "cuda" nếu có GPU ──
    model = load_model()
    embeddings = embed_segments(model, TRANSCRIPT_DATA)

    # Lưu embeddings để tái sử dụng (thực tế dùng Qdrant/FAISS)
    np.save("embeddings_cache.npy", embeddings)
    print("💾 Embeddings cached → embeddings_cache.npy\n")

    # ── Demo queries ──
    print("─" * 62)
    print("  📋 DEMO VỚI CÂU HỎI MẪU")
    print("─" * 62)
    for q in DEMO_QUERIES[:3]:
        t0 = time.time()
        results = search(q, model, TRANSCRIPT_DATA, embeddings, top_k=2)
        ms = (time.time() - t0) * 1000
        print(f"\n  ⚡ {ms:.1f}ms")
        print_results(q, results)

    # ── Interactive ──
    print("─" * 62)
    print("  🎮 TỰ NHẬP CÂU HỎI  (gõ 'q' để thoát)")
    print("─" * 62)
    print("\n  Gợi ý:")
    for q in DEMO_QUERIES:
        print(f"    • {q}")
    print()

    while True:
        try:
            query = input("  ❓ Câu hỏi: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not query or query.lower() in ("q", "quit", "exit"):
            break

        t0 = time.time()
        results = search(query, model, TRANSCRIPT_DATA, embeddings, top_k=3)
        ms = (time.time() - t0) * 1000
        print(f"  ⚡ {ms:.1f}ms")
        print_results(query, results)

    print("\n✅ Xong! Bước tiếp theo:")
    print("  1. Thay TRANSCRIPT_DATA bằng output Whisper thật")
    print("  2. Lưu embeddings vào Qdrant để scale lên nhiều video")
    print("  3. Bọc bằng FastAPI để tạo search API\n")
