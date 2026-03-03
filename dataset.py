# @author David Do
# created in 3/3/2026 10:12 PM
# description:

from dataclasses import dataclass


@dataclass
class Segment:
    id: int
    start: float  # giây
    end: float
    text: str
    video: str


@dataclass
class Segment:
    id: int
    start: float  # giây
    end: float
    text: str
    video: str


# Giả lập transcript của 2 video (thực tế sẽ dùng Whisper để tạo)
TRANSCRIPT_DATA = [
    # ── Video 1: Hội thảo về AI & Machine Learning ──
    Segment(0, 0.0, 12.0,
            "Xin chào mọi người, hôm nay chúng ta sẽ nói về ứng dụng của trí tuệ nhân tạo trong doanh nghiệp Việt Nam.",
            "hoi_thao_ai.mp4"),
    Segment(1, 12.0, 28.0,
            "Machine learning đang được áp dụng rộng rãi trong các bài toán dự đoán doanh thu, phân tích hành vi khách hàng.",
            "hoi_thao_ai.mp4"),
    Segment(2, 28.0, 45.0,
            "Mô hình deep learning như BERT và GPT đã thay đổi hoàn toàn cách chúng ta xử lý ngôn ngữ tự nhiên.",
            "hoi_thao_ai.mp4"),
    Segment(3, 45.0, 60.0,
            "Chi phí triển khai AI đang giảm đáng kể nhờ các dịch vụ cloud như AWS SageMaker, Google Vertex AI.",
            "hoi_thao_ai.mp4"),
    Segment(4, 60.0, 78.0, "Dữ liệu huấn luyện chất lượng cao là yếu tố then chốt quyết định độ chính xác của mô hình.",
            "hoi_thao_ai.mp4"),
    Segment(5, 78.0, 95.0,
            "Các công ty khởi nghiệp FinTech đang dùng AI để phát hiện gian lận giao dịch theo thời gian thực.",
            "hoi_thao_ai.mp4"),
    Segment(6, 95.0, 112.0, "Trong y tế, AI hỗ trợ bác sĩ chẩn đoán ung thư qua hình ảnh X-quang với độ chính xác 94%.",
            "hoi_thao_ai.mp4"),
    Segment(7, 112.0, 130.0, "Thách thức lớn nhất là thiếu nhân lực AI có kinh nghiệm, đặc biệt là kỹ sư MLOps.",
            "hoi_thao_ai.mp4"),
    Segment(8, 130.0, 148.0,
            "Chúng ta cần đầu tư vào giáo dục và đào tạo lại lực lượng lao động để thích nghi với kỷ nguyên AI.",
            "hoi_thao_ai.mp4"),

    # ── Video 2: Họp nội bộ chiến lược kinh doanh Q4 ──
    Segment(9, 0.0, 15.0, "Báo cáo doanh thu quý 3 đạt 125 tỷ đồng, tăng 18% so với cùng kỳ năm ngoái.",
            "hop_q4_strategy.mp4"),
    Segment(10, 15.0, 30.0, "Thị trường miền Nam tăng trưởng mạnh nhất với 25%, trong khi miền Bắc tăng 12%.",
            "hop_q4_strategy.mp4"),
    Segment(11, 30.0, 48.0,
            "Kế hoạch quý 4 tập trung vào mở rộng kênh bán hàng online và tăng cường marketing digital.",
            "hop_q4_strategy.mp4"),
    Segment(12, 48.0, 65.0, "Ngân sách marketing quý 4 được phê duyệt 8 tỷ đồng, tăng 30% so với quý trước.",
            "hop_q4_strategy.mp4"),
    Segment(13, 65.0, 82.0,
            "Chúng ta sẽ ra mắt 3 sản phẩm mới vào tháng 11, tập trung vào phân khúc khách hàng doanh nghiệp.",
            "hop_q4_strategy.mp4"),
    Segment(14, 82.0, 100.0,
            "Đội ngũ bán hàng cần được đào tạo thêm về kỹ năng tư vấn giải pháp công nghệ cho khách hàng B2B.",
            "hop_q4_strategy.mp4"),
    Segment(15, 100.0, 118.0, "Rủi ro chính trong quý 4 là sự cạnh tranh từ đối thủ nước ngoài và biến động tỷ giá.",
            "hop_q4_strategy.mp4"),
    Segment(16, 118.0, 135.0, "Chúng tôi đề xuất tăng giá bán 5% từ tháng 12 để bù đắp chi phí vận hành tăng.",
            "hop_q4_strategy.mp4"),
    Segment(17, 135.0, 152.0, "Mục tiêu doanh thu cả năm là 480 tỷ đồng, cần nỗ lực đạt 130 tỷ trong quý 4.",
            "hop_q4_strategy.mp4"),
]
